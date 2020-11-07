import time
from flask import Flask, request
#import fetch from 'isomorphic-fetch';

app=Flask(__name__)

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

if __name__ == '__main__':
    print("Initializing Server")
    app.run(debug = True)