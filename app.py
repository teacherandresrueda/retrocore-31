import streamlit as st

st.set_page_config(
    page_title="RetroCore 31",
    layout="centered"
)
# 🎨 estilo PRO
st.markdown("""
    <style>
    body {
        background-color: #0f172a;
    }
    .stApp {
        background: linear-gradient(135deg, #0f172a, #1e293b);
        color: white;
    }
    h1 {
        text-align: center;
        font-size: 48px;
    }
    .stButton>button {
        background-color: #22c55e;
        color: white;
        border-radius: 12px;
        padding: 10px;
        font-weight: bold;
    }
    .stTextInput>div>div>input {
        border-radius: 10px;
        padding: 10px;
    }
    </style>
""", unsafe_allow_html=True)
st.subheader("📥 Entrada")
st.text_input(...)

st.subheader("⚙️ Acciones")
st.button(...)

st.subheader("🎯 Resultado")
st.success(...)
st.markdown("<h1>🔥 RetroCore 31</h1>", unsafe_allow_html=True)
st.write("Sistema Inteligente • Melate Retro")

# 👉 input manual
numeros = st.text_input("Ingresa jugada (ej: 1,7,9,22,31,38)")

if st.button("Guardar jugada"):
    nums = list(map(int, numeros.split(",")))
    guardar_jugada(nums)
    st.success("Guardado 🔥")

# 👉 generar con IA
if st.button("Generar jugada personalizada"):
    jugada = generar_jugada_personalizada()
st.success(f"🎯 Jugada generada: {jugada}")
# 👉 ver historial
if st.checkbox("Ver historial"):
    data = cargar_historial()
    st.write(data["jugadas"])
