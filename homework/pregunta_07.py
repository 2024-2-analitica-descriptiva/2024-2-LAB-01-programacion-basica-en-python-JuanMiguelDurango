"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_07():
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla
    contiene un valor posible de la columna 2 y una lista con todas las letras
    asociadas (columna 1) a dicho valor de la columna 2.

    Rta/
    [(0, ['C']),
     (1, ['E', 'B', 'E']),
     (2, ['A', 'E']),
     (3, ['A', 'B', 'D', 'E', 'E', 'D']),
     (4, ['E', 'B']),
     (5, ['B', 'C', 'D', 'D', 'E', 'E', 'E']),
     (6, ['C', 'E', 'A', 'B']),
     (7, ['A', 'C', 'E', 'D']),
     (8, ['E', 'D', 'E', 'A', 'B']),
     (9, ['A', 'B', 'E', 'A', 'A', 'C'])]

    """

    import csv
    # Inicializar un diccionario para almacenar las letras asociadas a cada valor de la columna 2
    asociaciones = {}

    # Leer el archivo CSV
    with open("./files/input/data.csv") as csvfile:
        reader = csv.reader(csvfile, delimiter='\t')
        for row in reader:
            letra = row[0]
            valor = int(row[1])
            if valor in asociaciones:
                asociaciones[valor].append(letra)
            else:
                asociaciones[valor] = [letra]

    # Construir la lista de resultados
    resultado = []
    for valor in sorted(asociaciones.keys()):
        resultado.append((valor, asociaciones[valor]))

    return resultado

# Llamar a la función y mostrar el resultado
pregunta_07()