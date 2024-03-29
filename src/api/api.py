import os
from os import read
from flask import Flask, request, redirect, url_for, session, render_template
#import fetch from 'isomorphic-fetch';
from werkzeug.utils import secure_filename
import numpy as np
import search
import bacafile
import pandas as pd

UPLOAD_FOLDER = ''

app=Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
#@app.route('/time')
#def get_current_time():
#    return {'time': time.time(), 'id' : [13,14,15]}
print("initializing Server")
df = pd.DataFrame()
df2 = pd.DataFrame()
readfiles = False
#webscraping dan membersihkan dokumen
(doc1,title1,first1) = search.getDocuments2('https://www.tribunnews.com/')
(doc2,title2,first2) = search.getDocuments('https://kompas.com/')
doc = np.concatenate((doc1, doc2))
title = np.concatenate((title1, title2))
first = np.concatenate((first1, first2))
clean_doc = search.cleanDocuments(doc)
print("Server Ready")

@app.route('/query', methods=['POST'])
def Post_query():
    #query = request.form['query']
    query = request.get_json()
    print("query received",query)
    #print("query received",query)
    global doc
    global title
    global first
    global clean_doc
    global readfiles
    #Jika user mengupload file menggabungkan file hasil upload ke array dokumen
    if (readfiles):
        print("recalculating Sim")
        doc = np.concatenate((doc1, doc2))
        title = np.concatenate((title1, title2))
        first = np.concatenate((first1, first2))
        (doc3,title3,first3) = bacafile.getDocumentsFiles()
        doc = np.concatenate((doc, doc3))
        title = np.concatenate((title, title3))
        first = np.concatenate((first, first3))  
        clean_doc = search.cleanDocuments(doc)
        readfiles = False
        print("done recalculating Sim")

    global df
    global df2

    print("Calculating sim")
#    print("doc",doc)
#    print("clean_doc",clean_doc)
#    print("title",title)
    (df, df2) = search.search(query, clean_doc, title, first, doc) #Menghitung similarity
    print("done Calculating sim")
    print(df)

    #print(df2.to_html())
    return {"messege":"ok"}
@app.route('/tabel')
def Get_tabel():
    print("sending table")
    return {"content":df2.to_html()}
    #return {"content" : render_template('simple.html',  tables=[df.to_html(classes='data')], titles=df.columns.values)}
@app.route('/result')
def Get_result():
    print("ccontructiong result")
    result = df.to_numpy()
    #print(result)
    resultFinal = []
    panjang = 5
    if (len(result) < 5):
        panjang = len(result)
    for i in range(panjang):
        resultFinal.append({"sim":result[i][0],"title":result[i][1],"body":result[i][2],"count":result[i][3]})
    print(resultFinal)
    print("sending result")
    """
    return {"content" : [
        {"title":"Title1" ,"body":"Body1","sim":1,"count":100},
        {"title":"Title2" ,"body":"Body2","sim":2,"count":200},
        {"title":"Title3" ,"body":"Body3","sim":3,"count":300},
        {"title":"Title4" ,"body":"Body4","sim":4,"count":400},
        {"title":"Title5" ,"body":"Body5","sim":5,"count":500}
        ]
    }"""
    return {"content":resultFinal}     
    #data dummy (sementara matriks string dulu aja), sementara blm dibikin front endnya baru dikirim aja kalau mau liat di console
    #return {} #diisi yang bakal dikirim ke cllient

@app.route('/Get_Doc1')
def Get_Doc1():
    result = df.to_numpy()
    return {"title":result[0][1] ,"content":result[0][4]}
    
@app.route('/Get_Doc2')
def Get_Doc2():
    result = df.to_numpy()
    return {"title":result[1][1] ,"content":result[1][4]}

@app.route('/Get_Doc3')
def Get_Doc3():
    result = df.to_numpy()
    return {"title":result[2][1] ,"content":result[2][4]}

@app.route('/Get_Doc4')
def Get_Doc4():
    result = df.to_numpy()
    return {"title":result[3][1] ,"content":result[3][4]}

@app.route('/Get_Doc5')
def Get_Doc5():
    result = df.to_numpy()
    return {"title":result[4][1] ,"content":result[4][4]}


@app.route('/upload',methods=['POST'])
def Get_file():
    print("receiving file")
    target=os.path.join(UPLOAD_FOLDER,'docs')
    print(target)
    if not os.path.isdir(target):
        os.mkdir(target)
    file = request.files['file']
    print(file)
    #print(request.method)
    #print(request.files)
    filename = secure_filename(file.filename)
    destination="/".join([target, filename])
    file.save(destination)
    session['uploadFilePath']=destination
    global readfiles
    readfiles = True

    return "ok"



if __name__ == '__main__':
    #print("Initializing Server")
    app.secret_key = os.urandom(24)
    app.run(debug=True,use_reloader=False)