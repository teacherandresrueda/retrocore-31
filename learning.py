import json
import os

MODEL_FILE = "model.json"

def cargar_modelo():
    if not os.path.exists(MODEL_FILE):
        return {"w_freq": 2, "w_rec": 3, "w_cycle": 1}
    with open(MODEL_FILE, "r") as f:
        return json.load(f)

def guardar_modelo(modelo):
    with open(MODEL_FILE, "w") as f:
        json.dump(modelo, f)

def ajustar_pesos(modelo, aciertos):
    # simple refuerzo
    if aciertos >= 3:
        modelo["w_freq"] += 0.1
        modelo["w_rec"] += 0.1
    else:
        modelo["w_cycle"] += 0.1

    # limitar crecimiento
    modelo["w_freq"] = min(modelo["w_freq"], 5)
    modelo["w_rec"] = min(modelo["w_rec"], 5)
    modelo["w_cycle"] = min(modelo["w_cycle"], 5)

    guardar_modelo(modelo)
    return modelo
