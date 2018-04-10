# STDLIB
import json
import os

# third-party
from flask import Flask, request, abort, jsonify

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
        #TODO: Verificar se veio algo no request.json caso nada tenta o request.body (xml), caso nenhum dos 2 manda o peixe a merda 10/10
        # request.args << isso  o GET os args que vem com a URL depois do ? no path
        # request.data << isso  o XML
        # request.json << isso  adivinha? Hu3

        # TODO: Batch insert: Ler o JSON, se tiver uma lista como estrutura topo, ler cada item como sendo 1 sensor e ir inserindo as porra toda
        # Insere um sensor
        return str(insert_sensores(request.json))
    else:
        return 'Manda a mae! Aqui eh POST ou GET KRL!'