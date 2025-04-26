import numpy as np
import matplotlib.pyplot as plt # Librerías
# Definimos los puntos conocidos originalmente
Q = np.array([500, 700, 900, 1100, 1300, 1500, 1700, 1900])  # Q(l/h)
N = np.array([365, 361.6, 370.64, 379.68, 384.46, 395.5, 395.95, 397])  # N(w)

# Definimos la función que calcula la interpolación de Lagrange en un punto x
def lagrange_interpolation(x, X_points, Y_points):
    total = 0 # inicializamos la suma del polinomio en 0
    n = len(X_points)
    # Sumamos cada término Y_i * L_i(x) 
    for i in range(n):
        term = Y_points[i] # Empezamos con el coeficiente Y_i
        # Calculamos el producto para L_i(x)
        for j in range(n):
            if i != j: # Evitamos dividir entre 0
                term *= (x - X_points[j]) / (X_points[i] - X_points[j])
        total += term #Sumamos el término al polinomio
    return total # Devolvemos el valor interpolado en x
# Creamos un conjunto de puntos cercanos donde evaluaremos el polinomio
x_accumulation = np.linspace(min(Q), max(Q), 500)
# Evaluamos todos esos puntos cercanos con la función de interpolación
y_accumulation = np.array([lagrange_interpolation(x, Q, N) for x in x_accumulation])

# Graficamos una figura que se imprimirá en pantalla
plt.figure(figsize=(10, 6))
# Graficamos la curva de interpolación
plt.plot(x_accumulation, y_accumulation, label='Interpolación de Lagrange', color='blue')
# Graficamos los puntos originales
plt.scatter(Q, N, color='red', label='Puntos conocidos')
# Añadimos etiquetas
plt.title('Interpolación de Lagrange para los datos dados')
plt.xlabel('Q (l/h)')
plt.ylabel('N (w)')
# Añadimos cuadrícula, leyenda y mostramos
plt.grid(True)
plt.legend()
plt.show()