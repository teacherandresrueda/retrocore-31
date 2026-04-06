import json
import os

FILE = "historial.json"

def cargar_historial():
    if not os.path.exists(FILE):
        return {"jugadas": []}
    with open(FILE, "r") as f:
        return json.load(f)

def guardar_jugada(numeros):
    data = cargar_historial()
    data["jugadas"].append(numeros)
    with open(FILE, "w") as f:
        json.dump(data, f)
