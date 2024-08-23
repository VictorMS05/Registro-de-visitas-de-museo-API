"""Vista para la tabla visita"""
from flask import jsonify, request
from MySQLdb import OperationalError, IntegrityError


def consultar_visitas(cursor):
    """funcion para consultar las visitas al museo"""
    try:
        cursor.execute("USE museo")
        print(cursor)
        id_persona = request.args.get('id')
        consulta = "SELECT * FROM visitas"
        if id_persona:
            consulta = f"SELECT * FROM visitas WHERE id_persona = {id_persona}"
        print(consulta)
        cursor.execute(consulta)
        print("Entre")
        visitas = cursor.fetchall()
        print("Aqui si funciona")
        return jsonify({"success": True,
                        "status": 200,
                        "message": "tu consulta fue exitosa",
                        "data": visitas})
    except OperationalError as e:
        return jsonify({'error': {"code": 500,
                        "type": "error del servidor",
                        "message": "tu consulta tuvo error en la base de datos",
                        "details": str(e)}})
    
def registrar_visitas(cursor, conexion):
    """funcion para registrar las visitas al museo"""
    try:
        body = request.json
        cursor.execute("USE museo")
        cursor.execute("INSERT INTO visitas(nombres, email, telefono, fecha) values(%s, %s, %s, CURRENT_TIMESTAMP)", (body['nombres'], body['email'], body['telefono']))
        conexion.connection.commit()
        return jsonify({"success": True,
                        "status": 201,
                        "message": "La visita fue registrada exitosamente",
                        "data": body})
    except KeyError as e:
        return jsonify({'error': {"code": 400,
                        "type": "error del usuario",
                        "message": "escribiste algo mal en tu body",
                        "details": str(e)}})
    except IntegrityError as e:
        return jsonify({'error': {"code": 400,
                        "type": "error del usuario",
                        "message": "ingresaste mal un dato",
                        "details": str(e)}})
    except OperationalError as e:
        return jsonify({'error': {"code": 500,
                        "type": "error del servidor",
                        "message": "tu consulta tuvo error en la base de datos",
                        "details": str(e)}})

def actualizar_visitas(cursor, conexion, clave):
    """funcion para actualizar datos de las visitas"""
    try:
        body = request.json
        cursor.execute("USE museo")
        cursor.execute("SELECT id from visitas WHERE id = %i", clave)
        if cursor.fetchall()[0]:
            cursor.execute('UPDATE visitas SET nombres = %s, email = %s, telefono = %s WHERE id = %s',(body['nombres'], body['correo'], body['telefono'], clave))
            conexion.connection.commit()
            return jsonify({"success": True,
                        "status": 200,
                        "message": "La visita fue actualizada exitosamente",
                        "data": body})
        return jsonify({'error': {"code": 400,
                        "type": "error del usuario",
                        "message": "ingresaste mal el id",
                        }})
    except KeyError as e:
        return jsonify({'error': {"code": 400,
                        "type": "error del usuario",
                        "message": "escribiste algo mal en tu body",
                        "details": str(e)}})
    except IntegrityError as e:
        return jsonify({'error': {"code": 400,
                        "type": "error del usuario",
                        "message": "ingresaste mal un dato",
                        "details": str(e)}})
    except OperationalError as e:
        return jsonify({'error': {"code": 500,
                        "type": "error del servidor",
                        "message": "tu consulta tuvo error en la base de datos",
                        "details": str(e)}})

