import re
import string
from numpy.lib.function_base import vectorize
import requests
import numpy as np
import pandas as pd
from bs4 import BeautifulSoup
from sklearn.feature_extraction.text import TfidfVectorizer

vectorizer = TfidfVectorizer()

#Webscraping
def getDocuments(nama_web):
        r = requests.get(nama_web)

        soup = BeautifulSoup(r.content, 'html.parser')

        link = []
        for i in soup.find('div', {'class':'most__wrap'}).find_all('a'):
                i['href'] = i['href'] + '?page=all'
                link.append(i['href'])

        documents=[]
        for i in link:
                r = requests.get(i)

                soup = BeautifulSoup(r.content, 'html.parser')

                isi = []
                for i in soup.find('div', {'class':'read__content'}).find_all('p'):
                        isi.append(i.text)

                documents.append(' '.join(isi))

        return documents

def cleanDocuments(documents):
        clean = []
        for i in documents:
                document_test = re.sub(r'[^\x00-\x7F]+', ' ', i) #Menghilangkan unicode
                document_test = re.sub(r'@\w+', '', document_test) #menghilangkan mention
                document_test = document_test.lower() #Menjadikan semuanya huruf kecil
                document_test = re.sub(r'[%s]' % re.escape(string.punctuation), ' ', document_test) #Menghilangkan tanda baca
                document_test = re.sub(r'[0-9]', '', document_test) 
                document_test = re.sub(r'\s{2,}', ' ', document_test) #Menghilangkan dobel spasi

                clean.append(document_test)

        return clean

def create_dataframe(clean_documents):
        X = vectorizer.fit_transform(clean_documents)

        df = pd.DataFrame(X.T.toarray(), index=vectorizer.get_feature_names())

        return df

def search(query, df, doc):
        query = [query]
        q_vector = vectorizer.transform(query).toarray().reshape(df.shape[0],)
        print(q_vector)
        sim = {}
        for i in range(10):
                sim[i] = np.dot(df.loc[:, i].values, q_vector) / np.linalg.norm(df.loc[:,i])

        sorted_sim = sorted(sim.items(), key = lambda x: x[1], reverse = True)

        result = []
        for k,v in sorted_sim:
                if v != 0.0:
                        result.append((v, doc[k]))
        return result

doc = getDocuments('https://bola.kompas.com/')
doc1 = cleanDocuments(doc)
df = create_dataframe(doc1)
q = 'barcelona'
A = search(q, df, doc)
for i in A:
        x = i[0]
        y = i[1]
        print("sim = ", x)
        print(y)
        print("")
