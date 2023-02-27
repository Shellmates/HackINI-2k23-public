import os
from flag import FLAG
from tinymongo import TinyMongoClient
from flask import Flask, render_template, request, flash, redirect, url_for
from flask_cors import CORS
from gevent.pywsgi import WSGIServer

connection = TinyMongoClient('.')
db = connection.maSQLsh
secrets = db.secrets  

def init_db():
    secrets.remove({})  
    secret = {'username': 'admin', 'password': os.urandom(12).hex(), 'secret':FLAG}
    secrets.insert_one(secret)
    

def create_app():
    app = Flask(__name__)
    cors = CORS(app, resources={'/*': {"origins": "*"}})
    init_db()

    return app

app = create_app()


@app.route('/', methods=['GET','POST'])
def login(): 
    if request.method == 'POST':
        username = request.json['username']
        password = request.json['password']

        error = ''

        if not username:
            error = 'Username is required.'
        elif not password:
            error = 'Password is required.'
        else:
            query = {"$and":[{'username': username, 'password': password}]}
            user = secrets.find_one(query)

            if user is None:
                error = 'Wrong credentials.'

        if error:
            return error
        else:
            secret = user['secret']
            return secret

        
    return render_template('index.html')


if __name__ == "__main__":
    # Production
    print("starting the server ....")
    http_server = WSGIServer(('', 5000), app)
    print("Server is Up, enjoy :)")
    http_server.serve_forever()
