#%%
import time
from flask import Flask, redirect, url_for, request
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)
#%%
@app.route('/')
def server_check():
    return 'Server is running...'




#%%
cnt = [0]*200
@app.route('/get_signal/<id>')
def send_signal(id):
    global cnt
    id = int(id)
    print(request)
    cnt[id]+=1
    if cnt[id] % 2 == 0:
        return 'N'
    else:
        return 'S'


app.run(host="0.0.0.0",port="4000",debug=True)


