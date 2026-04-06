from collections import Counter
import random

# -------------------------
# ANALISIS BASE
# -------------------------
def analizar_frecuencia(historial):
    numeros = [n for fila in historial for n in fila]
    return Counter(numeros)

# -------------------------
# SCORE PREDICTIVO
# -------------------------
def calcular_score(historial):
    conteo = analizar_frecuencia(historial)

    score = {}

    # recencia (últimos sorteos pesan más)
    ultimos = historial[-3:]

    for num in range(1,40):
        frecuencia = conteo.get(num, 0)

        # recencia
        recencia = sum(1 for fila in ultimos if num in fila)

        # ciclo (si no aparece hace tiempo)
        ciclos = 0
        for fila in reversed(historial):
            if num not in fila:
                ciclos += 1
            else:
                break

        # fórmula de score
        score[num] = (
            frecuencia * 2 +      # peso histórico
            recencia * 3 +        # peso reciente
            min(ciclos, 5)        # peso ciclo (limitado)
        )

    return score

# -------------------------
# VALIDACION
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
# GENERADOR PREDICTIVO
# -------------------------
def generar_jugadas_predictivas(historial):
    score = calcular_score(historial)

    # ordenar por score
    ordenados = sorted(score, key=score.get, reverse=True)

    top = ordenados[:15]
    medio = ordenados[15:30]

    jugadas = []

    while len(jugadas) < 2:
        seleccion = []

        # 3 fuertes
        seleccion += random.sample(top, 3)

        # 2 medios
        seleccion += random.sample(medio, 2)

        # 1 aleatorio controlado
        seleccion += random.sample(range(1,40), 1)

        jugada = sorted(set(seleccion))

        if len(jugada) == 6 and validar_jugada(jugada):
            if jugada not in jugadas:
                jugadas.append(jugada)

    return jugadas, ordenados[:10]
