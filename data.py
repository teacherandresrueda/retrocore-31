historial = [
    [4,7,12,17,22,31,38],
    [7,8,12,19,22,31,38],
    [1,7,12,22,31,38],
    [3,4,5,19,21,31],
    [4,5,8,13,19,26],
    [3,6,7,8,33,37],
    [3,4,7,19,21,22,31],
    [9,19,23,24,27,38],
    [5,6,25,26,31,39],
    [17,18,29,31,34,39]
]
import streamlit as st
import random
import json
import os

st.set_page_config(page_title="Melate AI PRO", layout="centered")

# -------------------------
# LOGIN SIMPLE LOCAL (temporal)
# -------------------------
USER_FILE = "users.json"

def load_users():
    if os.path.exists(USER_FILE):
        with open(USER_FILE, "r") as f:
            return json.load(f)
    return {}

def save_users(users):
    with open(USER_FILE, "w") as f:
        json.dump(users, f)

users = load_users()

st.title("🔐 Melate AI PRO")

menu = st.selectbox("Menu", ["Login", "Register"])

if menu == "Register":
    user = st.text_input("Nuevo usuario")
    password = st.text_input("Contraseña", type="password")
    if st.button("Crear cuenta"):
        users[user] = password
        save_users(users)
        st.success("Cuenta creada")

if menu == "Login":
    user = st.text_input("Usuario")
    password = st.text_input("Contraseña", type="password")
    if st.button("Entrar"):
        if user in users and users[user] == password:
            st.success(f"Bienvenido {user}")

            st.subheader("🎲 Generador PRO")

            def generar():
                return sorted(random.sample(range(1, 57), 6))

            combo1 = generar()
            combo2 = generar()

            st.write("Combinación 1:", combo1)
            st.write("Combinación 2:", combo2)

            # HISTORIAL
            hist_file = f"{user}_historial.json"

            if st.button("Guardar jugada"):
                historial = []
                if os.path.exists(hist_file):
                    with open(hist_file, "r") as f:
                        historial = json.load(f)

                historial.append({
                    "combo1": combo1,
                    "combo2": combo2
                })

                with open(hist_file, "w") as f:
                    json.dump(historial, f)

                st.success("Guardado")

            if os.path.exists(hist_file):
                st.subheader("📊 Historial")
                with open(hist_file, "r") as f:
                    historial = json.load(f)
                    st.write(historial)

        else:
            st.error("Datos incorrectos")
