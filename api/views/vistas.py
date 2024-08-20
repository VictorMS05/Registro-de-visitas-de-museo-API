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
