import os
from flask import Flask, request, redirect, url_for, session
#import fetch from 'isomorphic-fetch';
from werkzeug.utils import secure_filename
import search 

UPLOAD_FOLDER = ''

app=Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
#@app.route('/time')
#def get_current_time():
#    return {'time': time.time(), 'id' : [13,14,15]}
print("wkwkwkwkw")

@app.route('/query', methods=['POST'])
def Post_query():
    #query = request.form['query']
    query = request.get_json()
    print("query received",query)
    #print("query received",query)
    (doc,title,first) = search.getDocuments2('https://www.tribunnews.com/')
    doc1 = search.cleanDocuments(doc)
    global df
    global df2
    print("Calculating sim")
    (df, df2) = search.search(query, doc1, title, first)
    print(df)
    return "ok"

@app.route('/result')
def Get_result():
    print("sending result")
    return {"content" : [
        {"title":"Title1" ,"body":"Body1","sim":1,"count":100},
        {"title":"Title2" ,"body":"Body2","sim":2,"count":200},
        {"title":"Title3" ,"body":"Body3","sim":3,"count":300},
        {"title":"Title4" ,"body":"Body4","sim":4,"count":400},
        {"title":"Title5" ,"body":"Body5","sim":5,"count":500}
        ]
    } #data dummy (sementara matriks string dulu aja), sementara blm dibikin front endnya baru dikirim aja kalau mau liat di console
    #return {} #diisi yang bakal dikirim ke cllient

@app.route('/upload',methods=['POST'])
def Get_file():
    print("receiving file")
    target=os.path.join(UPLOAD_FOLDER,'docs')
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

    return "ok"



if __name__ == '__main__':
    print("Initializing Server")
    app.secret_key = os.urandom(24)
    app.run(debug = True)