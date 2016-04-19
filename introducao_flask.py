# -*- enconding: UTF-8 -*-
import api

import requests

from flask import Flask, request, render_template

app = Flask(__name__)

from api_arquivo import ler_usuarios

@app.route('/')
def hello_world():
    return render_template('index.html', teste='pessoa')
    
@app.route('/login', methods={'GET', 'POST'})
def login():
    login = request.form['login']
    senha = request.form['senha']
    return render_template('home.html', filmes = api.request_filmes())

@app.route('/usuarios')
def usuarios():
    return render_template('usuarios.html', usuarios = ler_usuarios())

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)