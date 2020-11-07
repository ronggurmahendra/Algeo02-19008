import time
from flask import Flask

app=Flask(__name__)

@app.route('/time')
def get_current_time():
    return {'time': time.time(), 'id' : [13,14,15]}
print("hello WOrld !!!")