from core_ai import generar_jugadas_predictivas

st.subheader("🧠 IA Predictiva Nivel 13")

if st.button("🚀 Generar jugadas predictivas"):
    
    jugadas, top10 = generar_jugadas_predictivas(historial)
from learning import ajustar_pesos, cargar_modelo

# después de generar jugadas
if st.button("📥 Registrar resultado del sorteo"):
    resultado = st.text_input("Ingresa resultado (ej: 1,7,12,22,31,38)")

    if resultado:
        resultado = [int(x) for x in resultado.split(",")]

        aciertos = 0
        for j in jugadas:
            aciertos += len(set(j) & set(resultado))

        modelo = cargar_modelo()
        modelo = ajustar_pesos(modelo, aciertos)

        st.success(f"Aciertos: {aciertos}")
        st.write("Modelo actualizado:", modelo)
    st.write("🔥 Top números del día:")
    st.write(top10)

    st.subheader("🎯 Jugadas del día")

    for i, j in enumerate(jugadas):
        st.success(f"Jugada {i+1}: {j}")

    guardar_jugada(st.session_state.user, jugadas)

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
