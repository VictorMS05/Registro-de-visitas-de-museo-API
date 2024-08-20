"""Archivo principal de la API"""

from flask import Flask
from flask_mysqldb import MySQL
from flask_cors import CORS
from config import diccionario_de_configuraciones
from views import vistas

app = Flask(__name__)
CORS(app)
conexion = MySQL(app)


@app.route('/api/visitas')
def get():
    """Funcion para obtener visitas"""
    print("entre")
    cursor = conexion.connection.cursor()
    print(cursor)
    return vistas.consultar_visitas(cursor)


if __name__ == '__main__':
    app.config.from_object(diccionario_de_configuraciones['development'])
    app.run()
