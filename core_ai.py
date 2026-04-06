from collections import Counter
import random

# -------------------------
# ANALISIS FRECUENCIA
# -------------------------
def analizar_frecuencia(historial):
    numeros = [n for fila in historial for n in fila]
    conteo = Counter(numeros)
    return [num for num, _ in conteo.most_common()]

# -------------------------
# DETECCION AVANZADA
# -------------------------
def detectar_hot_cold(historial):
    numeros = [n for fila in historial for n in fila]
    conteo = Counter(numeros)

    # HOT = más frecuentes
    hot = [num for num, _ in conteo.most_common(6)]

    # COLD = menos frecuentes
    todos = set(range(1,40))
    usados = set(numeros)
    cold = list(todos - usados)

    if len(cold) < 6:
        cold = [num for num, _ in conteo.most_common()[-6:]]

    # REBOTE = último sorteo
    rebote = historial[-1]

    return hot, cold, rebote

# -------------------------
# VALIDACION MATEMATICA
# -------------------------
def validar_jugada(jugada):
    pares = sum(1 for n in jugada if n % 2 == 0)
    bajos = sum(1 for n in jugada if n <= 20)

    if pares < 2 or pares > 4:
        return False
    if bajos < 2 or bajos > 4:
        return False

    jugada.sort()
    consecutivos = sum(1 for i in range(len(jugada)-1) if jugada[i+1] - jugada[i] == 1)
    if consecutivos > 2:
        return False

    return True

# -------------------------
# GENERADOR NIVEL 12
# -------------------------
def generar_jugadas_avanzadas(historial):
    frecuentes = analizar_frecuencia(historial)
    hot, cold, rebote = detectar_hot_cold(historial)

    base = frecuentes[:3]  # núcleo fuerte

    jugadas = []

    while len(jugadas) < 2:
        seleccion = []

        # núcleo
        seleccion += random.sample(base, 3)

        # hot extra
        seleccion += random.sample(hot, 1)

        # cold
        seleccion += random.sample(cold, 1)

        # rebote
        seleccion += random.sample(rebote, 1)

        jugada = sorted(set(seleccion))

        if len(jugada) == 6 and validar_jugada(jugada):
            if jugada not in jugadas:
                jugadas.append(jugada)

    return jugadas, hot, cold, rebote
