"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """
    # Ruta del archivo
    archivo_csv = './files/input/data.csv'

    # Inicializar la suma
    suma = 0

    # Leer el archivo línea por línea
    with open(archivo_csv, 'r') as archivo:
        for linea in archivo:
            columnas = linea.strip().split("\t")  # Dividir la línea en columnas por tabulaciones
            try:
                suma += float(columnas[1])  # Convertir a float y sumar la segunda columna
            except (IndexError, ValueError):
                # Ignorar líneas sin una segunda columna válida o valores no numéricos
                pass

    return suma

pregunta_01()