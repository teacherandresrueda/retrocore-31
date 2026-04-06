from collections import Counter
import random

def analizar_frecuencia(historial):
    numeros = [n for fila in historial for n in fila]
    conteo = Counter(numeros)
    return [num for num, _ in conteo.most_common()]

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

def generar_2_jugadas_pro(historial):
    frecuentes = analizar_frecuencia(historial)

    top = frecuentes[:12]
    resto = list(set(range(1,40)) - set(top))

    jugadas = []

    while len(jugadas) < 2:
        base = random.sample(top, 4)
        extras = random.sample(resto, 2)
        jugada = sorted(base + extras)

        if validar_jugada(jugada) and jugada not in jugadas:
            jugadas.append(jugada)

    return jugadas
