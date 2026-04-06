from collections import Counter
from storage import cargar_historial
import random

def generar_jugada_personalizada():
    data = cargar_historial()
    jugadas = data["jugadas"]

    if not jugadas:
        return sorted(random.sample(range(1, 40), 6))

    # 🔥 contar frecuencia real
    todos = [num for jugada in jugadas for num in jugada]
    conteo = Counter(todos)

    # 🔥 top números fuertes
    top = [num for num, _ in conteo.most_common(12)]

    # 🔥 mezcla inteligente
    seleccion = random.sample(top, 4) + random.sample(range(1,40), 2)

    return sorted(seleccion)
