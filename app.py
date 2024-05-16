from flask import Flask, jsonify, request

import mariadb
import sys

# Importar configuración de acceso a la base de datos
from Back_end_Software import DATABASE_CONFIG

app = Flask(__name__)

try:
    conn = mariadb.connect(**DATABASE_CONFIG)
except mariadb.Error as e:
    print(f"Error en la conexión: {e}")
    sys.exit(1)

cursor = conn.cursor()


# Rutas para manejar la información de los clientes
@app.route('/api/clientes', methods=['GET'])
def obtener_clientes():
    cursor.execute("SELECT * FROM Clientes")
    lista_clientes = []
    for cliente in cursor.fetchall():
        lista_clientes.append({
            "id_cliente": cliente[0],
            "nombre": cliente[1],
            "apellido": cliente[2],
            "licencia_conduccion": cliente[3],
            "telefono": cliente[4],
            "correo": cliente [5]
        })
    return jsonify(lista_clientes)


@app.route('/api/clientes', methods=['POST'])
def agregar_cliente():
    datos_cliente = request.json
    nombre = datos_cliente.get('nombre')
    apellido = datos_cliente.get('apellido')
    licencia_conduccion = datos_cliente.get('licencia_conduccion')
    telefono = datos_cliente.get('telefono')
    correo = datos_cliente.get('correo')

    cursor.execute("INSERT INTO Clientes (nombre, apellido, licencia_conduccion, telefono, correo) VALUES (?, ?, ?, ?, ?)",
                   (nombre, apellido, licencia_conduccion, telefono, correo))
    conn.commit()

    return jsonify({'mensaje': 'Cliente agregado correctamente'})


# Rutas para manejar la información de los vehículos
@app.route('/api/vehiculos', methods=['GET'])
def obtener_vehiculos():
    cursor.execute("SELECT * FROM Vehiculo")
    lista_vehiculos = []
    for vehiculo in cursor.fetchall():
        lista_vehiculos.append({
            "id_vehiculo": vehiculo[0],
            "marca": vehiculo[1],
            "modelo": vehiculo[2],
            "año": vehiculo[3],
            "tarifa_diaria": vehiculo[4]
        })
    return jsonify(lista_vehiculos)


@app.route('/api/vehiculos', methods=['POST'])
def agregar_vehiculo():
    datos_vehiculo = request.json
    marca = datos_vehiculo.get('marca')
    modelo = datos_vehiculo.get('modelo')
    año = datos_vehiculo.get('año')
    tarifa_diaria = datos_vehiculo.get('tarifa_diaria')
    disponible = datos_vehiculo.get('disponible')

    cursor.execute("INSERT INTO Vehiculos (marca, modelo, año , tarifa_diaria, disponible) VALUES (?, ?, ?, ?, ?)",
                   (marca, modelo, año, tarifa_diaria, disponible))
    conn.commit()

    return jsonify({'mensaje': 'Vehículo agregado correctamente'})


# Rutas para manejar la información de los alquileres
@app.route('/api/alquileres', methods=['GET'])
def obtener_alquileres():
    cursor.execute("SELECT * FROM Alquileres")
    lista_alquileres = []
    for alquiler in cursor.fetchall():
        lista_alquileres.append({
            "id_alquiler": alquiler[0],
            "fecha_inicio": alquiler[1],
            "fecha_fin": alquiler[2],
            "id_vehiculo": alquiler[3],
            "id_cliente": alquiler[4]
        })
    return jsonify(lista_alquileres)


@app.route('/api/alquileres', methods=['POST'])
def agregar_alquiler():
    datos_alquiler = request.json
    fecha_inicio = datos_alquiler.get('fecha_inicio')
    fecha_fin = datos_alquiler.get('fecha_fin')
    id_vehiculo = datos_alquiler.get('id_vehiculo')
    id_cliente = datos_alquiler.get('id_cliente')

    cursor.execute("INSERT INTO Alquileres (fecha_inicio, fecha_fin, id_vehiculo, id_cliente) VALUES (?, ?, ?, ?)",
                   (fecha_inicio, fecha_fin, id_vehiculo, id_cliente))
    conn.commit()

    return jsonify({'mensaje': 'Alquiler registrado correctamente'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
