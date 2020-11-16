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
#Webscraping kompas.com
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
#Webscraping tribunnews.com
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
                
        link.pop(0)
        title.pop(0)

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
        query = stemmer.stem(query) #stemming query
        query = query.split() #memisahkan query menjadi kata-kata
        
        element = []
        #Membuat array element berisi elemen unik dari query
        for i in query:
                if i not in element:
                        element.append(i)
        #Membuat vektor query
        q_vector = [0 for i in range(len(element))]        
        for i in range (len(element)):
                for j in query:
                        if element[i] == j:
                                q_vector[i] += 1
        q_vector = np.array(q_vector)
        #Membuat vektor setiap dokumen dan juga menghitung banyak kata
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

        #Menghitung similarity
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
        
        #Membuat dataframe berisis similarity, judul, kalimat pertama, jumlah kata, dan dokumen
        data = {'similarity': similarity,
                'title' : title,
                'first': first,
                'jumlah kata': wordcount,
                'document': doc}

        df = pd.DataFrame(data, columns = ['similarity', 'title', 'first', 'jumlah kata', 'document'])
        df = df.sort_values(by=['similarity'], ascending=False)
        
        #Membuat dataframe tabel jumlah kata
        index = list(df.index.values)
        i = 5
        if len(index)<5:
                i = len(index)
        title1 = []
        vectors1= []
        for j in range (i):
                title1.append(title[index[j]])
                vectors1.append(vectors[index[j]])
        title1 = np.concatenate((['query'], title1))
        q_vector = [q_vector]
        vectors1 = np.concatenate((q_vector, vectors1))
        df2 = pd.DataFrame(vectors1, columns = element, index = title1)
        df2 = df2.T
        
        
        return (df, df2)


