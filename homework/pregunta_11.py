"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada
    letra de la columna 4, ordenadas alfabeticamente.

    Rta/
    {'a': 122, 'b': 49, 'c': 91, 'd': 73, 'e': 86, 'f': 134, 'g': 35}


    """

    import csv
    # Inicializar un diccionario para almacenar la suma de la columna 2 para cada letra de la columna 4
    suma_columna_2 = {}

    # Leer el archivo CSV
    with open("./files/input/data.csv") as csvfile:
        reader = csv.reader(csvfile, delimiter='\t')
        for row in reader:
            valor_columna_2 = int(row[1])
            columna_4 = row[3].split(',')
            for letra in columna_4:
                if letra in suma_columna_2:
                    suma_columna_2[letra] += valor_columna_2
                else:
                    suma_columna_2[letra] = valor_columna_2

    # Ordenar el diccionario por las letras
    suma_columna_2_ordenado = dict(sorted(suma_columna_2.items()))

    return suma_columna_2_ordenado

pregunta_11()