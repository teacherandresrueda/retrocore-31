import streamlit as st
from core_ai import generar_2_jugadas_pro
from data import historial
from auth import login, registrar
from storage import guardar_jugada, obtener_historial

st.set_page_config(page_title="RetroCore 31", layout="centered")

st.title("🔥 RetroCore 31")
st.write("Sistema Inteligente Melate Retro")

# -------------------------
# LOGIN
# -------------------------
if "user" not in st.session_state:
    opcion = st.radio("Selecciona", ["Login", "Registro"])

    user = st.text_input("Usuario")
    password = st.text_input("Contraseña", type="password")

    if opcion == "Registro":
        if st.button("Crear cuenta"):
            if registrar(user, password):
                st.success("Cuenta creada")
            else:
                st.error("Usuario ya existe")

    if opcion == "Login":
        if st.button("Entrar"):
            if login(user, password):
                st.session_state.user = user
            else:
                st.error("Datos incorrectos")

# -------------------------
# APP PRINCIPAL
# -------------------------
if "user" in st.session_state:

    st.success(f"Bienvenido {st.session_state.user}")

    if st.button("⚡ Generar jugadas del día"):
        jugadas = generar_2_jugadas_pro(historial)

        for i, j in enumerate(jugadas):
            st.success(f"Jugada {i+1}: {j}")

        guardar_jugada(st.session_state.user, jugadas)

    st.subheader("📊 Historial")
    hist = obtener_historial(st.session_state.user)

    for h in hist:
        st.write(h)

    if st.button("Cerrar sesión"):
        del st.session_state.user
