import os
from flask import Flask, request, redirect, url_for, session
#import fetch from 'isomorphic-fetch';
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = ''

app=Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
#@app.route('/time')
#def get_current_time():
#    return {'time': time.time(), 'id' : [13,14,15]}


@app.route('/query', methods=['POST'])
def Post_query():
    #query = request.form['query']
    query = request.get_json()
    #print("query received",query)
    
    print("query received")
    print(query)
    return "ok"

@app.route('/result')
def Get_result():
    print("sending result")
    return {"content" : [["title1","body1"],["title2","body2"],["title3","body3"]]} #data dummy (sementara matriks string dulu aja), sementara blm dibikin front endnya baru dikirim aja kalau mau liat di console
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