"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2
    por cada letra de la columa 1.

    Rta/
    [('A', 9, 2), ('B', 9, 1), ('C', 9, 0), ('D', 8, 3), ('E', 9, 1)]

    """
    file_path = './files/input/data.csv'
    maximos = {}
    minimos = {}

# Leer el archivo línea por línea
    with open(file_path, 'r') as file:
        for line in file:
            columns = line.strip().split("\t")  # Dividir por tabulaciones
            if len(columns) > 1:  # Asegurarse de que la línea tenga al menos dos columnas
                letra = columns[0]  # Obtener la letra de la primera columna
                try:
                    valor = int(columns[1])  # Convertir la segunda columna a entero
                    # Actualizar el valor máximo y mínimo para la letra correspondiente
                    if letra not in maximos or valor > maximos[letra]:
                        maximos[letra] = valor
                    if letra not in minimos or valor < minimos[letra]:
                        minimos[letra] = valor
                except ValueError:
                 pass  # Ignorar valores no numéricos

    # Combinar los valores máximos y mínimos en una lista de tuplas
    resultado_extremos = [(letra, maximos[letra], minimos[letra]) for letra in sorted(maximos.keys())]

    return resultado_extremos

pregunta_05()