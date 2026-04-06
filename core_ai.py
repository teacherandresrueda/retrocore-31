from collections import Counter
import random

def analizar_frecuencia(historial):
    numeros = [num for fila in historial for num in fila]
    conteo = Counter(numeros)
    return [num for num, _ in conteo.most_common()]

def generar_pool_29(frecuentes):
    base = frecuentes[:15]
    resto = list(set(range(1,40)) - set(base))
    extras = random.sample(resto, 14)
    return sorted(base + extras)

def generar_jugada(pool):
    return sorted(random.sample(pool, 6))

def generar_jugada_pro(nucleo, pool):
    base = random.sample(nucleo, len(nucleo))
    extras = list(set(pool) - set(base))
    seleccion = random.sample(extras, 2)
    return sorted(base + seleccion)
