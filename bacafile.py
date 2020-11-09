import os,sys,shutil
#baca dokumen dari satu dir
def getDocumentsFiles():
        #cari path
        d=os.getcwd()
        path=d+"\docs"
        #list nama file
        arr = os.listdir(path)
        os.chdir(path)
        documents=[]
        #loop untuk setiap file
        for x in arr:
            f=open(x,"r")
            isi = []
            for i in f:
                isi.append(i.strip("\n"))
            documents.append(' '.join(isi))
        f.close()
        return documents
doc=getDocumentsFiles()        
print(doc) 