#!/usr/bin/env python3

from flask import Flask, request
from hashlib import sha256	

app = Flask(__name__)

@app.route("/",methods=['GET', 'POST'])
def main():
	if request.method == 'GET':
		return {"message":"Welcome to shellpong services"}, 200
	else:
		try:
			score = int(request.json['score'])
			if (score == 100 and (sha256(b"shellmates").hexdigest()==request.json['token'])):
				return {"Flag":"shellmates{G4m35_h4ck1ng_15_fun}"}, 200
			else:
				return {"message":"Wrong score or token."}, 403
		except:
			return "some errors occured", 400

if __name__=="__main__":
	app.run('0.0.0.0',1337)
