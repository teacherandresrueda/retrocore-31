import streamlit as st
from core_ai import generar_jugadas_predictivas
from data import historial
from auth import login, registrar
from storage import guardar_jugada, obtener_historial
from learning import cargar_modelo

st.set_page_config(page_title="RetroCore 31", layout="wide")

# -------------------------
# ESTILO
# -------------------------
st.markdown("""
<style>
.main {
    background-color: #0e1117;
}
h1, h2, h3 {
    color: #00ff88;
}
</style>
""", unsafe_allow_html=True)

# -------------------------
# LOGIN
# -------------------------
if "user" not in st.session_state:
    st.title("🔐 RetroCore 31")

    opcion = st.radio("Acceso", ["Login", "Registro"])

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
# DASHBOARD
# -------------------------
if "user" in st.session_state:

    st.title("🔥 RetroCore 31 Dashboard")
    st.write(f"Bienvenido, {st.session_state.user}")

    col1, col2, col3 = st.columns(3)

    # -------------------------
    # IA GENERACIÓN
    # -------------------------
    if st.button("🚀 Generar jugadas IA"):
        jugadas, top10 = generar_jugadas_predictivas(historial)
        st.session_state.jugadas = jugadas
        st.session_state.top10 = top10

    if "top10" in st.session_state:
        col1.subheader("🔥 Top números IA")
        col1.write(st.session_state.top10)

    if "jugadas" in st.session_state:
        col2.subheader("🎯 Jugadas del día")
        for j in st.session_state.jugadas:
            col2.success(j)

    # -------------------------
    # MODELO
    # -------------------------
    modelo = cargar_modelo()

    col3.subheader("🧠 Modelo IA")
    col3.write(modelo)

    # -------------------------
    # HISTORIAL
    # -------------------------
    st.subheader("📊 Historial de jugadas")

    hist = obtener_historial(st.session_state.user)

    for h in hist[-10:]:
        st.write(h)

    # -------------------------
    # GUARDAR
    # -------------------------
    if "jugadas" in st.session_state:
        if st.button("💾 Guardar jugadas"):
            guardar_jugada(st.session_state.user, st.session_state.jugadas)
            st.success("Guardado")

    # -------------------------
    # LOGOUT
    # -------------------------
    if st.button("Cerrar sesión"):
        del st.session_state.user
