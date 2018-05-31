# STDLIB
import json
import os
#0.1
# third-party
from flask import Flask, abort, jsonify, render_template, flash, redirect, session, abort, request, redirect
import eventlet
import datetime
# local
from mysql_database import read_sensores, insert_sensores, read_usuarios, insert_usuario, read_carros, insert_carro, logincheck, read_carrosdia,read_carrostabela, updatesensor, read_carroscalendario
import time

eventlet.monkey_patch()
app = Flask(__name__, static_url_path='/static')


@app.route('/', methods=["GET", "POST"])
def login():
    if request.method == 'GET':
        return render_template('mapa.html')
    else:
        user=request.form['user']
        password=request.form['password']
        usuario = logincheck(user,password)
        idusuario = usuario[0]
    return redirect

@app.route('/relatorio_calendario')
def relatorio_calendario():
    return render_template('filtrocalendario.html')

@app.route('/relatoriocalendario')
def relatoriocalendario():
    return render_template('relatoriocalendario.html')

@app.route('/relatorio_tabela')
def relatorio_tabela():
    return render_template('filtrotabela.html')

@app.route('/relatorio_diario')
def relatorio_diario():
    return render_template('filtrorelatorioporhora.html')


@app.route('/alterar_sensor')
def alterar_sensor():
    return render_template('AlterarSensor.html')

@app.route('/calendario')
def carroscalendario():
    diai = request.args.get('di')
    diaf = request.args.get('df')
    id = request.args.get('id')
    return jsonify(read_carroscalendario(diai,diaf,id))

@app.route('/alterasensor', methods=["POST"])
def alterasensor():
    if request.method =='POST':
        aux = request.form
        # verificar usuario depois
        dados = {'idusuario': 1, 'lat': float(aux['lat']), 'idsensor': int(aux['idsensor']),
                 'lon': float(aux['lon']), 'nome': aux['Nome do sensor'], 'descricao': aux['Descrição']}
        updatesensor(dados)
    return redirect("/")


@app.route('/tabela')
def tabela():
    return render_template('tablechart.html')


@app.route('/relatoriodiario')
def graficodia():
    return render_template('linechart.html')

@app.route('/carrosdia')
def readcarrosdia():
    dia = request.args.get('dia')
    id = request.args.get('id')
    print(dia)
    print(id)
    return jsonify(read_carrosdia(dia, id))

@app.route('/carrostabela')
def readcarrostabela():
    dia = request.args.get('dia')
    id = request.args.get('id')
    print(dia)
    print(id)
    return jsonify(read_carrostabela(dia, id))




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
            #verificar usuario depois
            dados = {'idusuario': 1, 'lat': float(aux['lat']),
                     'lon': float(aux['lon']), 'nome': aux['Nome do sensor'], 'descricao': aux['Descrição']}
        else:
            dados = None

        if dados is not None:
            # Insere um sensor
            print(dados)
            insert_sensores(dados)
            return redirect("/")
        else:
            return 'ERRO 404'
    else:
        return 'ERRO 404'


@app.route('/cadastrar_sensor')
def cadastra_sensores():
    return render_template('CadastroSensores.html')

@app.route('/cadastra_usuarios')
def cadastra_usuario():
    return render_template('usuarios.html')

@app.route('/mapa')
def mapa():
    return render_template('mapa.html')


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
            return 'ERRO 404'
    else:
        return 'ERRO 404'

@app.route('/cadastra_carros')
def cadastra_carro():
    return render_template('carros.html')



@app.route('/carros', methods=['GET', 'POST'])
def carros():
    if request.method == 'GET':
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
            return ''
    else:
        return ''



if __name__ == '__main__':
    app.secret_key = os.urandom(12)
    app.run()
