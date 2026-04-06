
  from core_ai import generar_2_jugadas_pro
from data import historial

st.subheader("🔥 Jugadas del día (High Confidence)")

if st.button("⚡ Generar jugadas del día"):
    jugadas = generar_2_jugadas_pro(historial)

    for i, j in enumerate(jugadas):
        st.success(f"Jugada {i+1}: {j}")

# 🚀 MODO PRO
st.subheader("🚀 Modo PRO (núcleo fijo)")

if st.button("⚡ Generar jugadas PRO"):
    if "pool" in st.session_state:
        for i in range(5):
            st.write(generar_jugada_pro(NUCLEO, st.session_state.pool))
    else:
        st.warning("Primero genera el pool")
