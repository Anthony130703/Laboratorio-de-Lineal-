import matplotlib.pyplot as plt
import numpy as np

# Algoritmo de la eliminacion de gauss
def EliminacionGauss(matriz_X, vector_Y):

    num_X = len(matriz_X)

    # Algoritmo para crear la matriz aumtentada
    for i in range(num_X):
        matriz_X[i].append(vector_Y[i])
    
    # Creacion del algoritmo para poner la matriz en una matriz triangular superior
    for i in range(num_X):

        # encontrando el pivote que tiene que ser distinto de 0
        if matriz_X[i][i] == 0:
            for j in range(i+1, num_X):
                if matriz_X[j][i] != 0:
                    matriz_X[i], matriz_X[j] = matriz_X[j], matriz_X[i]
                    break
        
        # Haciendo 0 debajo de X[i][i]
        for j in range(i+1, num_X):
            razon = matriz_X[j][i] / matriz_X[i][i]
            for k in range(i, num_X+1):
                matriz_X[j][k] -= razon * matriz_X[i][k]
    
    # fin de ascalonar la matriz
    
    # obteniendo los coeficientes del polinomio
    solucion = [0] * num_X
    
    for i in range(num_X-1, -1, -1):
        suma = sum(matriz_X[i][j] * solucion[j] for j in range(i+1, num_X))
        solucion[i] = (matriz_X[i][num_X] - suma) / matriz_X[i][i]
    
    return solucion

# Datos a interpolar
Q = np.array([500, 700, 900, 1100, 1300, 1500, 1700, 1900], dtype=float)
N = np.array([365, 361.6, 370.64, 379.68, 384.46, 395.5, 395.95, 397], dtype=float)

# Encontrar el numero de datos
num_Q = len(Q)

# Construccion de la matriz ya en su forma con sus exponentes respectivos
matriz_X = [[Q[i]**j for j in range(num_Q)] for i in range(num_Q)]
vector_Y = list(N)

# Resolucion del sistema
coeficientes = EliminacionGauss([fila[:] for fila in matriz_X], vector_Y)

# Mostrar el polinomio Interpolado
polinomio = "P(x) = "
for i, coef in enumerate(coeficientes): # use la funcion enumerate para poder recorrer la lista de coeficientes
    if coef >= 0:
        polinomio += f"+ {coef:.6f}x^{i} " if i > 0 else f"{coef:.6f} "
    else:
        polinomio += f"- {abs(coef):.6f}x^{i} " if i > 0 else f"- {abs(coef):.6f} "

print("\nPolinomio resultante:")
print(polinomio)

# Graficar el polinomio
valores_Q = np.linspace(min(Q), max(Q), 400) # creando los espacios en la grafica en Q
valores_N = sum(c * valores_Q**i for i, c in enumerate(coeficientes)) #calculando los valores de N en su respectivo punto Q

plt.figure(figsize=(10, 6)) # ajustando la grafica a un tamaño 10x6
plt.plot(Q, N, 'ro', label='Datos') # haciendo los datos puntos rojos 
plt.plot(valores_Q, valores_N, 'b-', label='Polinomio interpolado') # haciendo la linea de la grafica de color azul y solida
# agregando los nombres a sus respectivos ejes
plt.xlabel("Q (l/h)")
plt.ylabel("N (w)")
plt.title("Interpolación polinómica(monomio)") #titulo
plt.legend() # mostrando la leyenda
plt.grid(True) # activando cuadricula en la grafica
plt.show() # dibujando el grafico 
