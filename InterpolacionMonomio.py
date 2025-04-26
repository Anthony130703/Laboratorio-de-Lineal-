import numpy as np

# Algoritmo de la eliminacion de gauss
def EliminacionGauss(X, Y):
    
    num_X= len(X)

    # Algoritmo para crear la matriz aumtentada
    for i in range(num_X):
        X[i].append(Y[i])
    
    # Creacion del algoritmo para poner la matriz en una matriz triangular superior
    for i in range (num_X):

        #encontrando el pivote que tiene que ser distinto de 0
        if X[i][i] == 0:
            for j in range(i+1, num_X):
                if X[j][i] != 0:
                    X[i], X[j] = X[j], X[i] #intercambiar las filas si se encuentra un 0 
                    break

        # Haciendo 0 debajo de X[i][i]
        for j in range(i+1, num_X):
            razon = X[j][i]/ X[i][j]
            for k in range(i, num_X+1):
                X[j][k] -= razon * X[i][k] 

    # fin de ascalonar la matriz

    # obteniendo los coeficientes del polinomio
    solucion = [0] * num_X

    for i in range(num_X-1, -1, -1):
        suma = 0
        
        for j in range(i+1, num_X):
            suma += X[i][j] * solucion[j]
            solucion[i] = (X[i][num_X] - suma)/X[i][j]

    return solucion

# Datos que se quiere interpolar por el monomio
Q = [500, 700, 900, 1100, 1300, 1500, 1700, 1900]
N = [365, 361.6, 370.64, 379.68, 384.46, 395.5, 395.95, 397]

# Encontrar el numero de datos
num_X = len(Q)

# Construccion de la matriz ya en su forma con sus exponentes respectivos
X = [[Q[i]**j for j in range(num_X)] for i in range(num_X)]
Y = list[N]

# Resolucion del sistema
coeficientes = EliminacionGauss([fila[:] for fila in X], Y)

# Mostrar el polinomio Interpolado
polinomio = "P(x) = "
