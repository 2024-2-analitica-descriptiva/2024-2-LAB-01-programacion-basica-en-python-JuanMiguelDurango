"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como
    una lista de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [('A', 53), ('B', 36), ('C', 27), ('D', 31), ('E', 67)]

    """

    # Inicializar un diccionario para sumar los valores de la segunda columna por cada letra
    from collections import Counter
    suma_por_letra = Counter()
    file_path = "./files/input/data.csv"

    # Leer el archivo línea por línea
    with open(file_path, 'r') as file:
        for line in file:
            columns = line.strip().split("\t")  # Dividir por tabulaciones
            if len(columns) > 1:  # Asegurarse de que la línea tenga al menos dos columnas
                letra = columns[0]  # Obtener la letra de la primera columna
                try:
                    valor = int(columns[1])  # Convertir la segunda columna a entero
                    suma_por_letra[letra] += valor  # Sumar el valor para la letra correspondiente
                except ValueError:
                    pass  # Ignorar valores no numéricos

    # Convertir el diccionario a una lista de tuplas, ordenada alfabéticamente
    resultado_suma = sorted(suma_por_letra.items())

    return resultado_suma

pregunta_03()