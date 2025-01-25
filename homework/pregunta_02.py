"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como
    la lista de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [('A', 8), ('B', 7), ('C', 5), ('D', 6), ('E', 14)]

    """
# Ruta del archivo
    file_path = './files/input/data.csv'

    # Contar la cantidad de registros por cada letra en la primera columna
    from collections import Counter

# Inicializar un contador para las letras de la primera columna
    counter = Counter()

# Leer el archivo línea por línea
    with open(file_path, 'r') as file:
        for line in file:
            columns = line.strip().split("\t")  # Dividir por tabulaciones
            if columns:  # Asegurarse de que la línea no esté vacía
                letra = columns[0]  # Obtener la letra de la primera columna
                counter[letra] += 1  # Contar la letra

# Convertir el contador a una lista de tuplas, ordenada alfabéticamente
    resultado = sorted(counter.items())

    return resultado

pregunta_02()