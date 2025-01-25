"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla
    contiene  el valor de la segunda columna; la segunda parte de la tupla
    es una lista con las letras (ordenadas y sin repetir letra) de la
    primera  columna que aparecen asociadas a dicho valor de la segunda
    columna.

    Rta/
    [(0, ['C']),
     (1, ['B', 'E']),
     (2, ['A', 'E']),
     (3, ['A', 'B', 'D', 'E']),
     (4, ['B', 'E']),
     (5, ['B', 'C', 'D', 'E']),
     (6, ['A', 'B', 'C', 'E']),
     (7, ['A', 'C', 'D', 'E']),
     (8, ['A', 'B', 'D', 'E']),
     (9, ['A', 'B', 'C', 'E'])]

    """

    from collections import defaultdict

# Crear un diccionario donde la clave es el valor de la segunda columna
# y el valor es un conjunto de letras únicas asociadas
    file_path = "./files/input/data.csv"
    valores_dict = defaultdict(set)

# Leer el archivo línea por línea
    with open(file_path, 'r') as file:
        for line in file:
            columns = line.strip().split("\t")  # Dividir por tabulaciones
            if len(columns) > 1:  # Asegurarse de que la línea tenga al menos dos columnas
                try:
                    valor = int(columns[1])  # Convertir la segunda columna a entero
                    letra = columns[0]  # Obtener la letra de la primera columna
                    valores_dict[valor].add(letra)  # Asociar la letra al valor
                except ValueError:
                    pass  # Ignorar valores no numéricos

    # Convertir el diccionario en una lista de tuplas, ordenando las letras alfabéticamente
    resultado_tuplas = [(valor, sorted(list(letras))) for valor, letras in sorted(valores_dict.items())]

    return resultado_tuplas

pregunta_08()