#%%
from flask import Flask, redirect, url_for, request
from flask_cors import CORS
import json
app = Flask(__name__)
CORS(app)
#%%

@app.route('/')
def server_start():
   return 'Server is running...'

@app.route('/success/<name>')
def login_success(name):
   return 'You are logged in.. {}'.format(name)

@app.route('/login',methods = ['GET','POST'])
def login():
   if request.method == 'POST':
        print(request)
        print('\n--------------------------------------\n\n')
        print(request.form)
        print('\n--------------------------------------\n\n')
        un = request.form['un']
        pwd = request.form['pwd']
        return redirect(url_for('login_success',name = un))



@app.route('/client',methods = ['GET','POST'])
def client():
   if request.method == 'POST':
      print(request)
      print('\n--------------------------------------\n\n')
      print(request.json)
      print('\n--------------------------------------\n\n')
      if request.json.__contains__('latitude') and request.json.__contains__('longitude'):
         lat = request.json['latitude']
         lng = request.json['longitude']
         if lat!=None and lng != None and lat!='' and lng != '':   
               print('{}\n{}\n-----------success----------------\n'.format(lat,lng))
               return json.dumps({'status' : 200})
         else:   
               print('\n\n-----------fail----------------\n')
               return json.dumps({'status' : 400})
      else:
         return json.dumps({'status' : 404,'description' : 'Keys not found'})





if __name__ == '__main__':
    app.run(host = '0.0.0.0',port = 4000,debug = True)

#%%




