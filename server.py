# STDLIB
import json
import os
#0.1
# third-party
from flask import Flask, request, abort, jsonify, render_template

# local
from mysql_database import read_sensores, insert_sensores

app = Flask(__name__)


@app.route('/')
def name_zuado():
    # Debug
    print('roda porra roda')
    return 'rodou krl da porra D:'


@app.route('/sensores', methods=['GET', 'POST'])
def sensores():
    if request.method == 'GET':
        # TODO: Vericicar parametros do GET, se no tiver nada devolver todos, caso tenha um parametro chamado id devolver 1 sensor que tenha o ID
        # Devolve todos sensores
        return jsonify(read_sensores())
    elif request.method == 'POST':
        # Verifica se tem um JSON no POST, caso no tenha procura no FORM
        if request.json is not None:
            dados = request.json
        elif request.form is not None:
            aux = request.form
            dados = {'idsensores': int(aux['idsensores']), 'idusuario': int(aux['idusuario']), 'lat': float(aux['lat']),
                     'lon': float(aux['lon']), 'nome': aux['nome'], 'descricao': aux['descricao']}
        else:
            dados = None

        if dados is not None:
            # Insere um sensor
            return str(insert_sensores(dados))
        else:
            return 'Se voce nao manda nada vou iserir oq? Teu cu?ahta'
    else:
        return 'Manda a mae! Aqui eh POST ou GET KRL!'


@app.route('/html')
def index():
    return render_template('teste.html')


@app.route('/cadastra_sensores')
def cadastra_sensores():
    return render_template('sensores.html')
