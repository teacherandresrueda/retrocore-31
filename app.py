import streamlit as st
from core_ai import analizar_frecuencia, generar_pool_29, generar_jugada, generar_jugada_pro
from data import historial, NUCLEO

st.set_page_config(page_title="RetroCore 31", layout="centered")

# 🎨 HEADER
st.markdown("<h1 style='text-align: center; color: #00ff88;'>RetroCore 31</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center;'>Sistema Inteligente Melate Retro</h4>", unsafe_allow_html=True)

# 📊 ANALISIS
frecuentes = analizar_frecuencia(historial)

st.subheader("📊 Núcleo detectado")
st.write(NUCLEO)

st.subheader("🔥 Top números frecuentes")
st.write(frecuentes[:10])

# 🎯 BOTON POOL
if st.button("🔥 Generar Pool 29"):
    pool = generar_pool_29(frecuentes)
    st.session_state.pool = pool
    st.success(pool)

# 🎯 USO DEL POOL
if "pool" in st.session_state:
    pool = st.session_state.pool

    st.subheader("🎯 Pool activo")
    st.write(pool)

    if st.button("🎟️ Generar 5 jugadas"):
        for i in range(5):
            st.write(generar_jugada(pool))

# 🚀 MODO PRO
st.subheader("🚀 Modo PRO (núcleo fijo)")

if st.button("⚡ Generar jugadas PRO"):
    if "pool" in st.session_state:
        for i in range(5):
            st.write(generar_jugada_pro(NUCLEO, st.session_state.pool))
    else:
        st.warning("Primero genera el pool")
