import matplotlib.pyplot as plt
import numpy as np
from sympy import symbols, expand #Librerias

#  Datos a interpolar

Q = [500, 700, 900, 1100, 1300, 1500, 1700, 1900]  # X
N = [365, 361.6, 370.64, 379.68, 384.46, 395.5, 395.95, 397]  # Y

#volviendo esta variable de forma simbolica para expresiones algebraicas a imrpimir en el polinomio de lagrange
x = symbols('x')

#Metodo de interpolacion de Newton 

def construir_matriz_newton(x_vals):
    
    #construyendo la matriz triangular inferior para el metodo de newton
    n = len(x_vals) #esta es una variable local de esta funcion
    A = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        A[i][0] = 1 # Primera columna siempre 1
        for j in range(1, i + 1):
            producto = 1
            for k in range(j):
                producto *= (x_vals[i] - x_vals[k])
            A[i][j] = producto
    return A

#sustitución hacia adelante (para matriz triangular inferior)
def sustitucion_adelante(A, Y):
    n = len(Y) #esta es otra variable local de esta funcion
    a = [0 for _ in range(n)]

    for i in range(n):
        suma = 0
        for j in range(i):
            suma += A[i][j] * a[j]
        a[i] = (Y[i] - suma) / A[i][i]
    return a

#imprimiendo el polinomio simbolicamente
def imprimir_polinomio_newton(coeficientes, x_vals):
    n = len(coeficientes) # esta es otra variable local de esta funcion
    polinomio = f"{coeficientes[0]:.6f}"
    for i in range(1, n):
        termino = f"{coeficientes[i]:+,.6f}"
        for j in range(i):
            termino += f"*(x - {x_vals[j]:.6f})"
        polinomio += " " + termino
    print("\nPolinomio de Newton (forma simbólica):")
    print("P(x) =", polinomio)

#evaluando el polinomio de Newton en un valor dado
def evaluar_newton(x_vals, coeficientes, x_eval):
    n = len(coeficientes) # variable local propia de esta funcion
    resultado = coeficientes[0]
    for i in range(1, n):
        producto = coeficientes[i]
        for j in range(i):
            producto *= (x_eval - x_vals[j])
        resultado += producto
    return resultado

# Metodo de interpolacion de Monomios 
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

#Metodo de interpolacion de Lagrange 

def polinomio_lagrange(Q, N):
    n = len(Q) # Esta variable es distinta a las de arriba, es de esta funcion
    # Inicializamos una lista para almacenar los valores L_i(x)
    L = []
    # Calculamos los términos L_i(x) para cada valor de i (Cada punto)
    for i in range(n):
        num = 1 # Numerador de L_i(x)
        den = 1 # Denominador de L_i(x)
        # Calculamos la productoria para el numerador y denominador
        for j in range(n):
            if i != j: # Evitamos dividir entre 0
                num *= (x - Q[j])
                den *= (Q[i] - Q[j])
        # Calculamos L_i(x) y lo multiplicamos por el valor correspondiente de y_i
        L.append(N[i] * num / den)
    # El polinomio es la suma de estos productos simbólicos
    polinomio = sum(L)
    return expand(polinomio)

#Newton (Wido)
#construiyendo la matriz A y resolver el sistema
A_newton = construir_matriz_newton(Q)
coef_newton = sustitucion_adelante(A_newton, N)

#mostrando los coeficientes
print("\nCoeficientes del Polinomio de Newton:")
for i, a in enumerate(coef_newton):
    print(f"a_{i} = {a:.6f}")

#mostranado el polinomio en su forma simbolica
imprimir_polinomio_newton(coef_newton, Q)

#  Monomios (Anthony)

# Encontrando el numero de datos
num_Q = len(Q)

# Construccion de la matriz ya en su forma con sus exponentes respectivos
matriz_X = [[Q[i]**j for j in range(num_Q)] for i in range(num_Q)]
vector_Y = list(N)

# Resolucion del sistema
coef_monomios = EliminacionGauss([fila[:] for fila in matriz_X], vector_Y)

print("\nCoeficientes del Polinomio de Monomios:")
for i, coef in enumerate(coef_monomios):
    print(f"a_{i} = {coef:.6f}")

# Imprimir polinomio de monomios
polinomio_monomios = f"{coef_monomios[0]:.6f}"
for i in range(1, len(coef_monomios)):
    if coef_monomios[i] >= 0:
        polinomio_monomios += f" + {coef_monomios[i]:.6f}x^{i}"
    else:
        polinomio_monomios += f" - {abs(coef_monomios[i]):.6f}x^{i}"

print("\nPolinomio de Monomios (forma simbólica):")
print("P(x) =", polinomio_monomios)

#Lagrange (Gabriel)

polinomio_lag = polinomio_lagrange(Q, N)

print("\nPolinomio de Lagrange :")
print(polinomio_lag)

# Grafica combinada de los polinomios

x_graf = np.linspace(min(Q), max(Q), 400)

# Evaluaciones de los puntos
y_newton = [evaluar_newton(Q, coef_newton, xi) for xi in x_graf]
y_monomios = sum(c * x_graf**i for i, c in enumerate(coef_monomios))
y_lagrange = [float(polinomio_lag.subs(x, val)) for val in x_graf]

# Gráfica
plt.figure(figsize=(12, 8))
plt.plot(Q, N, 'ro', label='Datos originales')
plt.plot(x_graf, y_newton, 'b-', linewidth=2, label='Polinomio de Newton')
plt.plot(x_graf, y_monomios, 'g--', linewidth=2, label='Polinomio de Monomios')
plt.plot(x_graf, y_lagrange, 'm-.', linewidth=2, label='Polinomio de Lagrange')
plt.title("Interpolación polinómica")
plt.xlabel("Q (l/h)")
plt.ylabel("N (w)")
plt.legend()
plt.grid(True)
plt.show()
