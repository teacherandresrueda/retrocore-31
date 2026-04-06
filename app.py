import streamlit as st
import json
import os
import random
from collections import Counter

# --------------------------
# CONFIG
# --------------------------
st.set_page_config(page_title="RetroCore 31", layout="centered")

# --------------------------
# ESTILO PRO
# --------------------------
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #0f172a, #1e293b);
    color: white;
}
h1 {
    text-align: center;
}
.stButton>button {
    background-color: #22c55e;
    color: white;
    border-radius: 10px;
    padding: 10px;
}
</style>
""", unsafe_allow_html=True)

# --------------------------
# STORAGE
# --------------------------
FILE = "historial.json"

def cargar_historial():
    if not os.path.exists(FILE):
        return {"jugadas": []}
    with open(FILE, "r") as f:
        return json.load(f)

def guardar_jugada(nums):
    data = cargar_historial()
    data["jugadas"].append(nums)
    with open(FILE, "w") as f:
        json.dump(data, f)

# --------------------------
# IA
# --------------------------
def generar_jugada():
    data = cargar_historial()
    jugadas = data["jugadas"]

    if not jugadas:
        return sorted(random.sample(range(1, 40), 6))

    todos = [n for j in jugadas for n in j]
    conteo = Counter(todos)

    top = [num for num, _ in conteo.most_common(12)]

    seleccion = random.sample(top, min(4, len(top))) + random.sample(range(1,40), 2)

    return sorted(seleccion)

# --------------------------
# UI
# --------------------------
st.markdown("<h1>🔥 RetroCore 31</h1>", unsafe_allow_html=True)
st.write("Sistema Inteligente • Melate Retro")

st.divider()

# INPUT
entrada = st.text_input("Ingresa jugada (ej: 1,7,9,22,31,38)")

st.divider()

# BOTONES
col1, col2 = st.columns(2)

with col1:
    if st.button("Guardar jugada"):
        try:
            nums = list(map(int, entrada.split(",")))
            if len(nums) == 6:
                guardar_jugada(nums)
                st.success("Guardado correctamente 🔥")
            else:
                st.error("Debes ingresar 6 números")
        except:
            st.error("Formato inválido")

with col2:
    if st.button("Generar jugada"):
        jugada = generar_jugada()
        st.success(f"🎯 {jugada}")

st.divider()

# HISTORIAL
if st.checkbox("Ver historial"):
    data = cargar_historial()
    st.write(data["jugadas"])
