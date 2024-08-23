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

@app.route('/api/visitas', methods=['POST'])
def post():
    """Funcion para registrar visitas"""
    cursor = conexion.connection.cursor()
    return vistas.registrar_visitas(cursor,  conexion)

@app.route('/api/visitas/<int:id>', methods=['PUT'])
def put(id):
    """funcion para actualizar las visitas del museo"""
    cursor= conexion.connection.cursor()
    return vistas.actualizar_visitas(cursor, conexion, id)

if __name__ == '__main__':
    app.config.from_object(diccionario_de_configuraciones['development'])
    app.run()
