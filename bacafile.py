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
        title=[]
        frstsntc=[]
        #loop untuk setiap file
        for x in arr:
            f=open(x,"r")
            isi = []
            counter=0
            for i in f:
                if counter==0:
                    title.append(i.strip("\n"))
                    counter=counter+1
                elif counter==1:
                    frstsntc.append(i.strip("\n"))
                isi.append(i.strip("\n"))
            documents.append(' '.join(isi))
        f.close()
        print(title)
        print(frstsntc) 
        return (documents,title,frstsntc)
# doc=getDocumentsFiles()        
# print(doc)
