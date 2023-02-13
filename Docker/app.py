from flask import Flask
from flask_mysqldb import MySQL
import os
import logging


app = Flask(__name__)

logging.basicConfig(level=logging.DEBUG)


logging.info('Conectando a base de datos')
try:
    app.config['MYSQL_USER'] = os.environ['MYSQL_USER']
    app.config['MYSQL_PASSWORD'] = os.environ['MYSQL_PASSWORD']
    app.config['MYSQL_HOST'] = os.environ['MYSQL_HOST']
    app.config['MYSQL_DB'] = os.environ['MYSQL_DB']
    mysql = MySQL(app)
except Exception as error:
    logging.error('Error conectando a base de datos' + str(error))

##########################################################################################################
@app.route('/')
def health():
    return 'App Python OK'
    
##########################################################################################################
@app.route('/inicializa-contador')
def initialize():
    logging.info('Inicializando contador')
    try: 
        cursor = mysql.connection.cursor()
        cursor.execute(''' UPDATE tabla_contador SET contador=0; ''')
        cursor.execute(''' COMMIT; ''')
        cursor.close()
        return 'Contador inicializado a 0'
    except Exception as error:
        logging.error('Error inicializando contador' + str(error))
        return 'Contador NO inicializado a 0'

##########################################################################################################
@app.route('/incrementar-contador')
def conteo():
    logging.info('Inicializando el conteo de visitas')

    try:
        s = "<table style='border:1px solid red'>"

        cursor = mysql.connection.cursor()
        cursor.execute(''' UPDATE tabla_contador SET contador = contador + 1; ''')
        cursor.execute(''' COMMIT; ''')
        cursor.close()
                                     
        cursor2 = mysql.connection.cursor()
        cursor2.execute(''' SELECT * FROM tabla_contador; ''')
        for row in cursor2.fetchall():
            s = s + "<tr>"
            for x in row:
                s = s + "<td>" + str(x) + "</td>"
            s = s + "</tr>"
        cursor2.close()
        return "<html><body> VISITANTES: " + s + "</body></html>"
    except Exception as error:
        logging.error('Error inicializando el conteo de visitas' + str(error))

############################################################################################
@app.route('/actual')
def getAll():
    logging.info('Obteniendo valor actual')

    try:
        cursor = mysql.connection.cursor()
        cursor.execute(''' SELECT * FROM tabla_contador; ''')
        myresult = cursor.fetchall()    
        cursor.close()
        return str(myresult)
    except Exception as error:
        logging.error('Error obteniendo valor actual')
        return 'Error obteniendo valor actual'