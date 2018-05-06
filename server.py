# STDLIB
import json
import os
#0.1
# third-party
from flask import Flask, request, abort, jsonify, render_template
import eventlet
import datetime
# local
from mysql_database import read_sensores, insert_sensores, read_usuarios, insert_usuario, read_carros, insert_carro
import time

eventlet.monkey_patch()
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
            print(dados)
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

@app.route('/cadastra_usuarios')
def cadastra_usuario():
    return render_template('usuarios.html')

@app.route('/usuarios', methods=['GET', 'POST'])
def usuarios():
    if request.method == 'GET':
        # TODO: Vericicar parametros do GET, se no tiver nada devolver todos, caso tenha um parametro chamado id devolver 1 sensor que tenha o ID
        # Devolve todos sensores
        return jsonify(read_usuarios())
    elif request.method == 'POST':
        # Verifica se tem um JSON no POST, caso no tenha procura no FORM
        if request.json is not None:
            dados = request.json
        elif request.form is not None:
            aux = request.form
            dados = {'idusuarios': int(aux['idusuario']), 'nome': (aux['nome']), 'status': int(aux['status']),
                     'login': (aux['login']), 'senha': aux['senha'], 'email': aux['email']}
        else:
            dados = None

        if dados is not None:
            # Insere um sensor
            return str(insert_usuario(dados))
        else:
            return 'Se voce nao manda nada vou iserir oq? Teu cu?ahta'
    else:
        return 'Manda a mae! Aqui eh POST ou GET KRL!'

@app.route('/cadastra_carros')
def cadastra_carro():
    return render_template('carros.html')

@app.route('/carros', methods=['GET', 'POST'])
def carros():
    if request.method == 'GET':
        # TODO: Vericicar parametros do GET, se no tiver nada devolver todos, caso tenha um parametro chamado id devolver 1 sensor que tenha o ID
        # Devolve todos sensores
        return jsonify(read_carros())
    elif request.method == 'POST':
        # Verifica se tem um JSON no POST, caso no tenha procura no FORM
        if request.json is not None:
            dados = request.json
            idsensor = dados.get('id')
            str_horarios = dados.get('passagens')
            list_horarios = str_horarios.split(',')
            ids = []
            for horario in list_horarios:
                print(horario)
                carro = {'idsensor': idsensor, 'horario': horario}
                str(insert_carro(carro))
            return jsonify(read_carros())
        elif request.form is not None:
            dados = request.form
            idsensor = dados.get('id')
            str_horarios = dados.get('passagens')
            list_horarios = str_horarios.split(',')
            for horario in list_horarios:
                now = datetime.datetime.now().strftime("%Y-%m-%d " + horario)
                carro = {'idsensor': idsensor, 'horario': now}
                str(insert_carro(carro))
            return jsonify(read_carros())
        else:
            return 'Se voce nao manda nada vou iserir oq? Teu cu?ahta'
    else:
        return 'Manda a mae! Aqui eh POST ou GET KRL!'


if __name__ == '__main__':
    app.run()
