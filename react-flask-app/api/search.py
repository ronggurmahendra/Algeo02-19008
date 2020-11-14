import re
import string
from numpy.core.defchararray import title
import requests
import numpy as np
import pandas as pd
from bs4 import BeautifulSoup
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
#import dari file lain
import bacafile

factory = StemmerFactory()
stemmer = factory.create_stemmer()
#Webscraping
def getDocuments(nama_web):
        r = requests.get(nama_web)

        soup = BeautifulSoup(r.content, 'html.parser')

        link = []
        title=[]
        for i in soup.find('div', {'class':'most__wrap'}).find_all('a'):
                i['href'] = i['href'] + '?page=all'
                link.append(i['href'])
        
        for i in soup.find('div', {'class':'most__wrap'}).find_all('h4'):
                temp=i.string.strip('<h4 class="most__title">')
                temp=i.string.strip('</h4>')
                temp.strip()
                title.append(temp)
                # print(temp)
                # print(i)
                # print(type(i))

        frstsntc=[]
        documents=[]
        j=0
        for i in link:
                r = requests.get(i)

                soup = BeautifulSoup(r.content, 'html.parser')

                isi = []
                for i in soup.find('div', {'class':'read__content'}).find_all('p'):
                        isi.append(i.text)
                kalimat = isi[0].split(". ")
                frstsntc.append(kalimat[0])
                isi = np.concatenate(([title[j]], isi))
                documents.append(' '.join(isi))
                j+=1
        return (documents,title,frstsntc)

def getDocuments2(nama_web):
        r = requests.get(nama_web)

        soup = BeautifulSoup(r.content, 'html.parser')

        link = []
        title=[]
        for i in soup.find('div', {'class':'mb20 populer'}).find_all('a'):
                # i['href'] = 'http://' + i['href'] #+?page=all'
                i['href'] = i['href']
                if i['href'].startswith('https://'):
                        link.append(i['href'])
        
        for i in soup.find('div', {'class':'mb20 populer'}).find_all('a'):
                if i['title'] not in title: 
                        title.append(i['title'])
                # print(temp)
                # print(i)
                # print(type(i))
        link.pop(0)
        title.pop(0)
        # print(link)
        # print(title)

        frstsntc=[]
        documents=[]
        j = 0
        for i in link:
                r = requests.get(i)

                soup = BeautifulSoup(r.content, 'html.parser')

                isi = []
                for i in soup.find('div', {'class':'side-article txt-article'}).find_all('p'):
                        isi.append(i.text)
                kalimat = isi[0].split(". ")
                frstsntc.append(kalimat[0])
                isi = np.concatenate(([title[j]], isi))
                documents.append(' '.join(isi))
                j+=1
        return (documents,title,frstsntc)

def cleanDocuments(documents):
        clean = []

        for i in documents:
                document_test = re.sub(r'[^\x00-\x7F]+', ' ', i) #Menghilangkan unicode
                document_test = re.sub(r'@\w+', '', document_test) #menghilangkan mention
                document_test = document_test.lower() #Menjadikan semuanya huruf kecil
                document_test = re.sub(r'[%s]' % re.escape(string.punctuation), ' ', document_test) #Menghilangkan tanda baca
                document_test = re.sub(r'[0-9]', '', document_test) 
                document_test = re.sub(r'\s{2,}', ' ', document_test) #Menghilangkan dobel spasi
                document_test = stemmer.stem(document_test)

                clean.append(document_test)

        return clean


def search(query, doc1, title, first, doc):
        query = stemmer.stem(query)
        query = query.split()
        
        element = []
        
        for i in query:
                if i not in element:
                        element.append(i)
        
        q_vector = [0 for i in range(len(element))]        
        for i in range (len(element)):
                for j in query:
                        if element[i] == j:
                                q_vector[i] += 1
        q_vector = np.array(q_vector)
        
        vectors = []
        wordcount = []
        for i in doc1:
                v1 = [0 for i in range (len(element))]
                i = i.split()
                wordcount.append(len(i))
                for j in i:
                        for k in range(len(element)):
                                if j == element[k]:
                                        v1[k] += 1
                                        break
                v1 = np.array(v1)
                vectors.append(v1)

        #print(vectors)

        similarity = []
        q_norm = np.linalg.norm(q_vector)
        for i in vectors:
                norm = np.linalg.norm(i)
                if norm != 0:
                        sim = np.dot(i, q_vector)/ (q_norm * norm)
                        sim *= 100
                else:
                        sim = 0
                similarity.append(sim)
        #print(similarity)

        data = {'similarity': similarity,
                'title' : title,
                'first': first,
                'jumlah kata': wordcount,
                'document': doc}

        df = pd.DataFrame(data, columns = ['similarity', 'title', 'first', 'jumlah kata', 'doc'])
        df = df.sort_values(by=['similarity'], ascending=False)
        #print(df)

        title = np.concatenate((['query'], title))
        q_vector = [q_vector]
        vectors = np.concatenate((q_vector, vectors))
        df2 = pd.DataFrame(vectors, columns = element, index = title)
        df2 = df2.T
        #print(df2)
        
        return (df, df2)

# (doc,title,first) = getDocuments('https://detik.com/')
# (doc,title,first) = getDocuments('https://kompas.com/')
#(doc,title,first) = getDocuments2('https://www.tribunnews.com/')
# # (doc, title, first)=bacafile.getDocumentsFiles()
#doc1 = cleanDocuments(doc)
# #print(doc[1])
# #print(doc1[1])
# (doc1,title1,first1) = getDocuments2('https://www.tribunnews.com/')
# (doc2,title2,first2) = getDocuments('https://kompas.com/')
# (doc3,title3,first3) = bacafile.getDocumentsFiles()
# doc = np.concatenate((doc1, doc2))
# doc = np.concatenate((doc, doc3))
# title = np.concatenate((title1, title2))
# title = np.concatenate((title, title3))
# first = np.concatenate((first1, first2))
# first = np.concatenate((first, first3))
# clean_doc = cleanDocuments(doc)
# q = 'polisi memenangkan monopoli Palsu mobil'
# (df, df2) = search(q, clean_doc, title, first)
# print(df)
# print(df2)
# #print(doc1)
