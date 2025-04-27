import matplotlib.pyplot as plt
import numpy as np

# Construir matriz triangular inferior para Newton
def construir_matriz_newton(x):
    n = len(x)
    A = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        A[i][0] = 1  # Primera columna siempre 1
        for j in range(1, i + 1):
            producto = 1
            for k in range(j):
                producto *= (x[i] - x[k])
            A[i][j] = producto
    return A

# Sustitución hacia adelante (para matriz triangular inferior)
def sustitucion_adelante(A, Y):
    n = len(Y)
    a = [0 for _ in range(n)]

    for i in range(n):
        suma = 0
        for j in range(i):
            suma += A[i][j] * a[j]
        a[i] = (Y[i] - suma) / A[i][i]
    return a

# Imprimir el polinomio simbólicamente
def imprimir_polinomio(coeficientes, x_vals):
    n = len(coeficientes)
    polinomio = f"{coeficientes[0]:.4f}"
    for i in range(1, n):
        termino = f"{coeficientes[i]:+,.4f}"
        for j in range(i):
            termino += f"*(x - {x_vals[j]:.4f})"
        polinomio += " " + termino
    print("\nPolinomio de Newton (forma simbólica):")
    print("P(x) =", polinomio)

# Evaluar el polinomio de Newton en un valor dado
def evaluar_newton(x_vals, coeficientes, x):
    n = len(coeficientes)
    resultado = coeficientes[0]
    for i in range(1, n):
        producto = coeficientes[i]
        for j in range(i):
            producto *= (x - x_vals[j])
        resultado += producto
    return resultado

# Datos de los 8 puntos dados
x = [500, 700, 900, 1100, 1300, 1500, 1700, 1900]
y = [365, 361.6, 370.64, 379.68, 384.46, 395.5, 395.95, 397]

# Construir matriz A y resolver el sistema
A = construir_matriz_newton(x)
coeficientes = sustitucion_adelante(A, y)

# Mostrar coeficientes
print("\nCoeficientes del polinomio de Newton (forma productoria):")
for i, a in enumerate(coeficientes):
    print(f"a_{i} = {a}")

# Mostrar el polinomio en forma simbólica
imprimir_polinomio(coeficientes, x)

# Graficar
x_graf = np.linspace(min(x) , max(x) , 400)
y_graf = [evaluar_newton(x, coeficientes, xi) for xi in x_graf]

plt.figure(figsize=(10, 6))
plt.plot(x_graf, y_graf, label="Polinomio de Newton", color='blue')
plt.scatter(x, y, color='red', label="Puntos dados")
plt.title("Interpolación por el Polinomio de Newton")
plt.xlabel("Q")
plt.ylabel("N")
plt.legend()
plt.grid(True)
plt.show()