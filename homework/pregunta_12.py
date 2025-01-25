"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor
    la suma de los valores de la columna 5 sobre todo el archivo.

    Rta/
    {'A': 177, 'B': 187, 'C': 114, 'D': 136, 'E': 324}

    """

    import csv
    # Inicializar un diccionario para almacenar la suma de los valores de la columna 5 para cada letra de la columna 1
    suma_columna_5 = {}

    # Leer el archivo CSV
    with open("./files/input/data.csv") as csvfile:
        reader = csv.reader(csvfile, delimiter='\t')
        for row in reader:
            letra = row[0]
            columna_5 = row[4].split(',')
            suma_valores = sum(int(par.split(':')[1]) for par in columna_5)
            if letra in suma_columna_5:
                suma_columna_5[letra] += suma_valores
            else:
                suma_columna_5[letra] = suma_valores

    return suma_columna_5

# Llamar a la función y mostrar el resultado
pregunta_12()