"""Archivo principal de la API"""

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    """Función que retorna un saludo"""
    return "<a>Hola Mundo!</a>"

@app.route('/comidas')
def comidas():
    """Función que retorna una lista de comidas"""
    return ['Tacos', 'Pizza', 'Hamburguesa', 'Sushi', 'Pasta', 'Ensalada', 'Pescado']

@app.route('/comidas/<int:id>')
def comida(id):
    """Función que retorna una comida específica"""
    comidas = ['Tacos', 'Pizza', 'Hamburguesa', 'Sushi', 'Pasta', 'Ensalada', 'Pescado']
    if id < len(comidas):
        return comidas[id]
    else:
        return 'Comida no encontrada'
    
@app.route('/saludo/persona')
def saludo_persona():
    """Función que retorna un saludo a una persona"""
    return 'Hola, persona!'

if __name__ == '__main__':
    app.run(debug=True)
