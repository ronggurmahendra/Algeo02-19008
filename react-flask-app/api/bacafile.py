import os,sys,shutil
import numpy as np
#baca dokumen dari satu dir
def getDocumentsFiles():
        #cari path
        d=os.getcwd()
        path=d+"\docs"
        #list nama file
        arr = os.listdir(path)
        os.chdir(path)
        documents=[]
        title=[]
        frstsntc=[]
        #loop untuk setiap file
        j = 0
        for x in arr:
            f=open(x,"r")
            isi = []
            counter=0
            for i in f:
                if counter==0:
                    title.append(i.strip("\n"))
                    counter=counter+1
                else:
                    isi.append(i.strip("\n"))
    
            kalimat = isi[0].split(". ")
            frstsntc.append(kalimat[0])
            isi = np.concatenate((title[j], isi))
            documents.append(' '.join(isi))
            j+=1
        f.close()
        #print(title)
        #print(frstsntc)
        #print(documents)
        #print(documents) 
        return (documents,title,frstsntc)
# doc=getDocumentsFiles()        
# print(doc)


