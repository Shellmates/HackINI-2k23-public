#!/usr/bin/python3
from flask import Flask, Response, redirect, request, jsonify, render_template, make_response,render_template_string
import json


app = Flask(__name__)


@app.route("/", methods=["GET","POST"])
def root():
    resp = make_response("<html><head></head><body>shellmates{Shunkun_Ido}</body></html>")
    resp.headers['Location'] = 'index'
    resp.status_code = 302
    return resp
@app.route("/index", methods=["GET","POST"])
def index():
    return render_template("index.html")
