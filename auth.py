import json
import os

USERS_FILE = "users.json"

def cargar_usuarios():
    if not os.path.exists(USERS_FILE):
        return {}
    with open(USERS_FILE, "r") as f:
        return json.load(f)

def guardar_usuarios(users):
    with open(USERS_FILE, "w") as f:
        json.dump(users, f)

def registrar(usuario, password):
    users = cargar_usuarios()
    if usuario in users:
        return False
    users[usuario] = {"password": password}
    guardar_usuarios(users)
    return True

def login(usuario, password):
    users = cargar_usuarios()
    if usuario in users and users[usuario]["password"] == password:
        return True
    return False
