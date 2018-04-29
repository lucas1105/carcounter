# Third-party
import mysql.connector
from mysql.connector import errorcode, connection

#0.1

def connect():
    try:
        cnx = connection.MySQLConnection(user='root', password='admin',
                                         host='127.0.0.1',
                                         database='carcounter')
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    else:
        return cnx


# Le todos os sensores (mistirei portugues com ingles)
def read_sensores():
    # Connect to database
    cnx = connect()

    # Creates a cursor (object used to read from gotten streams)
    cursor = cnx.cursor()

    # String da query
    query = ("SELECT * FROM sensores")

    cursor.execute(query)
    print(cursor)

    # Dict pra retornar um JSON no webserver
    sensores_list = []

    for (idsensores, idusuario, lat, lon, nome, descricao) in cursor:
        sensores_list.append({'idsensor': idsensores, 'idusuario': idusuario, 'lat': lat, 'lon': lon, 'nome': nome,
                         'descricao': descricao})

    cursor.close()
    cnx.close()

    sensores = {'sensores':sensores_list}

    return sensores

def read_usuarios():
    # Connect to database
    cnx = connect()

    # Creates a cursor (object used to read from gotten streams)
    cursor = cnx.cursor()

    # String da query
    query = ("SELECT * FROM usuarios")

    cursor.execute(query)
    print(cursor)

    # Dict pra retornar um JSON no webserver
    usuarios_list = []

    for (idusuarios, nome, status, login, senha, email) in cursor:
        usuarios_list.append({'idusuario': idusuarios, 'nome': nome, 'status': status, 'login': login, 'senha': senha,
                         'email': email})

    cursor.close()
    cnx.close()

    usuarios = {'usuarios':usuarios_list}

    return usuarios

def read_carros():
    # Connect to database
    cnx = connect()

    # Creates a cursor (object used to read from gotten streams)
    cursor = cnx.cursor()

    # String da query
    query = ("SELECT * FROM carros")

    cursor.execute(query)


    # Dict pra retornar um JSON no webserver
    carros_list = []

    for (idcarros, horario, idsensor) in cursor:
        carros_list.append({'idcarros': idcarros, 'idsensor':idsensor , 'horario': horario})

    cursor.close()
    cnx.close()

    carros = {'carros':carros_list}

    return carros

def insert_carro(carro):
    """
    Funcao para inserir um sensor no banco. Lucas viado essa porra aceita dict tbm dict mesma merda que JSON quase

    :param sensor: dict contendo os dados de um sensor
    :type sensor: dict
    :return:
    """

    cnx = connect()

    cursor = cnx.cursor()
    query = ("INSERT INTO carros (horario, idsensor) "
             "VALUES (%(horario)s,%(idsensor)s)")

    # Insert new employee
    cursor.execute(query, carro)
    idcarro = cursor.lastrowid

    # Make sure data is committed to the database
    cnx.commit()

    cursor.close()
    cnx.close()
    return idcarro

def insert_sensores(sensor):
    """
    Funcao para inserir um sensor no banco. Lucas viado essa porra aceita dict tbm dict mesma merda que JSON quase

    :param sensor: dict contendo os dados de um sensor
    :type sensor: dict
    :return:
    """

    cnx = connect()

    cursor = cnx.cursor()

    query = ("INSERT INTO sensores (idsensores, idusuario, lat, lon, nome, descricao) "
             "VALUES (%(idsensores)s, %(idusuario)s, %(lat)s, %(lon)s, %(nome)s, %(descricao)s)")

    # Insert new employee
    print(sensor)
    cursor.execute(query, sensor)
    idsensor = cursor.lastrowid

    # Make sure data is committed to the database
    cnx.commit()

    cursor.close()
    cnx.close()
    return idsensor

def insert_usuario(usuario):
    """
    Funcao para inserir um sensor no banco. Lucas viado essa porra aceita dict tbm dict mesma merda que JSON quase

    :param sensor: dict contendo os dados de um sensor
    :type sensor: dict
    :return:
    """

    cnx = connect()

    cursor = cnx.cursor()

    query = ("INSERT INTO usuarios (idusuarios, nome, status, login, senha, email) "
             "VALUES (%(idusuarios)s, %(nome)s, %(status)s, %(login)s, %(senha)s, %(email)s)")

    # Insert new employee
    print(usuario)
    cursor.execute(query, usuario)
    idusuario = cursor.lastrowid

    # Make sure data is committed to the database
    cnx.commit()

    cursor.close()
    cnx.close()
    return idusuario
