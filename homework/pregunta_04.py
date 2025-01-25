"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la
    cantidad de registros por cada mes, tal como se muestra a continuación.

    Rta/
    [('01', 3),
     ('02', 4),
     ('03', 2),
     ('04', 4),
     ('05', 3),
     ('06', 3),
     ('07', 5),
     ('08', 6),
     ('09', 3),
     ('10', 2),
     ('11', 2),
     ('12', 3)]

    """

    # Ruta del archivo
    file_path = './files/input/data.csv'

    # Contar la cantidad de registros por cada letra en la primera columna
    from collections import Counter

    # Inicializar un contador para los meses
    mes_counter = Counter()

    # Leer el archivo línea por línea
    with open(file_path, 'r') as file:
        for line in file:
            columns = line.strip().split("\t")  # Dividir por tabulaciones
            if len(columns) > 2:  # Asegurarse de que la línea tenga al menos tres columnas
                fecha = columns[2]  # Obtener la fecha de la tercera columna
                try:
                    mes = fecha.split("-")[1]  # Extraer el mes de la fecha (segundo elemento)
                    mes_counter[mes] += 1  # Contar el mes
                except IndexError:
                    pass  # Ignorar filas con fechas mal formateadas

    # Convertir el contador a una lista de tuplas, ordenada alfabéticamente por el mes
    resultado_meses = sorted(mes_counter.items())

    return resultado_meses

pregunta_04()