import pandas as pd
import win32com.client as win32

"""
    Flask = Framework -> criar site
"""
    # ferramente para criação dos sites
from flask import Flask, render_template
from flask_socketio import SocketIO, send

app = Flask(__name__) # criando o app
socketio = SocketIO(app, cors_allowed_origins="*") # criando o socketIO

    # funcionalidade de enviar mensagem
@socketio.on("message")
def gerenciar_mensagem(mensagem):
    send(mensagem, broadcast=True)

    # criando a 1º página = 1º rota
    # aqui é iniciada a primeira rota
@app.route("/")
    # esta função esta sendo atribuida a rota 1 acima
def homepage():
    return render_template("homepage.html")
    # roda o app
socketio.run(app, host="192.168.100.170")