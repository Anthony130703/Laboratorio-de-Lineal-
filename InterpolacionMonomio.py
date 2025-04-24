import numpy as np

# Datos que se quiere interpolar por el monomio
Q = [500, 700, 900, 1100, 1300, 1500, 1700, 1900]
N = [365, 361.6, 370.64, 379.68, 384.46, 395.5, 395.95, 397]

# Encontrar el numero de datos
num_datos = len(Q)

# Construccion de la matriz ya en su forma con sus exponentes respectivos
X = [[Q[i]**j for j in range(num_datos)] for i in range(num_datos)]
Y = list[N]

# Algoritmo de la eliminacion de gauss
def EliminacionGauss(X, Y, num_datos):
    
    # Algoritmo para crear la matriz aumtentada
    for i in range(num_datos):
        X[i].append(Y[i])
    
    # Creacion del algoritmo para poner la matriz en una matriz triangular superior
    for i in range (num_datos):

        #encontrando el pivote que tiene que ser distinto de 0
        if X[i][i] == 0:
            for j in range(i+1, num_datos):
                if X[j][i] != 0:
                    X[i], X[j] = X[j], X[i]
                    break

        # Haciendo 0 debajo de X[i][i]
        