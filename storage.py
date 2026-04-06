import json
import os

DATA_FILE = "data_users.json"

def cargar_data():
    if not os.path.exists(DATA_FILE):
        return {}
    with open(DATA_FILE, "r") as f:
        return json.load(f)

def guardar_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f)

def guardar_jugada(usuario, jugadas):
    data = cargar_data()

    if usuario not in data:
        data[usuario] = []

    data[usuario].append(jugadas)
    guardar_data(data)

def obtener_historial(usuario):
    data = cargar_data()
    return data.get(usuario, [])
