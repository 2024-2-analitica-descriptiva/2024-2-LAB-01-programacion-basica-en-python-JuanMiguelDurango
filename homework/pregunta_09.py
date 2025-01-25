"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que
    aparece cada clave de la columna 5.

    Rta/
    {'aaa': 13,
     'bbb': 16,
     'ccc': 23,
     'ddd': 23,
     'eee': 15,
     'fff': 20,
     'ggg': 13,
     'hhh': 16,
     'iii': 18,
     'jjj': 18}}

    """

    import csv
    # Inicializar un diccionario para almacenar la cantidad de registros por clave
    conteos = {}

    # Leer el archivo CSV
    with open("./files/input/data.csv") as csvfile:
        reader = csv.reader(csvfile, delimiter='\t')
        for row in reader:
            # Obtener la columna 5
            columna_5 = row[4]
            # Dividir la columna 5 en pares clave:valor
            pares = columna_5.split(',')
            for par in pares:
                clave, valor = par.split(':')
                if clave in conteos:
                    conteos[clave] += 1
                else:
                    conteos[clave] = 1

    return conteos

pregunta_09()