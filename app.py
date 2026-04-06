import streamlit as st
from storage import guardar_jugada, cargar_historial
from core_ai import generar_jugada_personalizada

st.title("RetroCore 31 🔥")

# 👉 input manual
numeros = st.text_input("Ingresa jugada (ej: 1,7,9,22,31,38)")

if st.button("Guardar jugada"):
    nums = list(map(int, numeros.split(",")))
    guardar_jugada(nums)
    st.success("Guardado 🔥")

# 👉 generar con IA
if st.button("Generar jugada personalizada"):
    jugada = generar_jugada_personalizada()
    st.write("🎯 Jugada:", jugada)

# 👉 ver historial
if st.checkbox("Ver historial"):
    data = cargar_historial()
    st.write(data["jugadas"])
