"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras
    corresponde a una clave y el valor despues del caracter `:` corresponde al
    valor asociado a la clave. Por cada clave, obtenga el valor asociado mas
    pequeño y el valor asociado mas grande computados sobre todo el archivo.

    Rta/
    [('aaa', 1, 9),
     ('bbb', 1, 9),
     ('ccc', 1, 10),
     ('ddd', 0, 9),
     ('eee', 1, 7),
     ('fff', 0, 9),
     ('ggg', 3, 10),
     ('hhh', 0, 9),
     ('iii', 0, 9),
     ('jjj', 5, 17)]

    """
    import csv
 #Inicializar un diccionario para almacenar los valores mínimos y máximos
    valores = {}

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
                valor = int(valor)
                if clave in valores:
                    valores[clave].append(valor)
                else:
                    valores[clave] = [valor]

    # Construir la lista de resultados
    resultado = []
    for clave in sorted(valores.keys()):
        min_valor = min(valores[clave])
        max_valor = max(valores[clave])
        resultado.append((clave, min_valor, max_valor))

    return resultado

# Llamar a la función y mostrar el resultado
pregunta_06()
