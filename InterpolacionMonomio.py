import matplotlib.pyplot as plt
import numpy as np

# Función de eliminación gaussiana con impresión de la matriz escalonada
def gauss_elimination(X, Y):
    n = len(X)

    # Crear matriz aumentada
    for i in range(n):
        X[i].append(Y[i])

    # Paso 1: Transformar a forma triangular superior
    for i in range(n):
        if X[i][i] == 0:
            for j in range(i+1, n):
                if X[j][i] != 0:
                    X[i], X[j] = X[j], X[i]
                    break
        for j in range(i+1, n):
            ratio = X[j][i] / X[i][i]
            for k in range(i, n+1):
                X[j][k] -= ratio * X[i][k]

    print("\nMatriz escalonada (forma triangular superior):")
    for fila in X:
        print(["{:.4f}".format(num) for num in fila])

    # Paso 2: Sustitución hacia atrás
    solution = [0] * n
    for i in range(n-1, -1, -1):
        sum_ = 0
        for j in range(i+1, n):
            sum_ += X[i][j] * solution[j]
        solution[i] = (X[i][n] - sum_) / X[i][i]

    return solution

# Leer datos desde archivo
datos = np.loadtxt("data1.txt", float)
Q = datos[:, 0]
N = datos[:, 1]
n = len(Q)

# Construir matriz X con monomios y vector Y
X = [[Q[i]**j for j in range(n)] for i in range(n)]
Y = list(N)

# Resolver sistema
coeficientes = gauss_elimination([fila[:] for fila in X], Y)

# Mostrar polinomio
polinomio = "P(x) = "
for i, coef in enumerate(coeficientes):
    if coef >= 0:
        polinomio += f"+ {coef:.6f}x^{i} " if i > 0 else f"{coef:.6f} "
    else:
        polinomio += f"- {abs(coef):.6f}x^{i} " if i > 0 else f"- {abs(coef):.6f} "

print("\nPolinomio resultante:")
print(polinomio)

# Graficar
x_vals = np.linspace(min(Q), max(Q), 400)
y_vals = sum(c * x_vals**i for i, c in enumerate(coeficientes))

plt.figure(figsize=(10, 6))
plt.plot(Q, N, 'ro', label='Datos')
plt.plot(x_vals, y_vals, 'b-', label='Polinomio interpolado')
plt.xlabel("Q (l/h)")
plt.ylabel("N (w)")
plt.title("Interpolación polinómica con eliminación gaussiana")
plt.legend()
plt.grid(True)
plt.show()
