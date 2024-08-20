"""Archivo de la conexión a la base de datos"""
import os
from dotenv import load_dotenv


class Configuracion():
    """clase para comenzar con la configuracion a la base de datos"""
    load_dotenv()
    DEBUG = True
    MYSQL_HOST = os.getenv('MYSQL_HOST')
    print(MYSQL_HOST)
    MYSQL_USER = os.getenv('MYSQL_USER')
    print(MYSQL_USER)
    MYSQL_PASSWORD = os.getenv('MYSQL_PASSWORD')
    print(MYSQL_PASSWORD)
    MYSQL_BD = os.getenv('MYSQL_BD')
    print(MYSQL_BD)
    MYSQL_PORT = int(os.getenv('MYSQL_PORT'))
    print(MYSQL_PORT)


diccionario_de_configuraciones = {
    'development': Configuracion
}
