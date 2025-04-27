from sympy import symbols
import matplotlib.pyplot as plt
import numpy as np
from sympy import *

# Definimos los puntos conocidos originalmente
Q = [500, 700, 900, 1100, 1300, 1500, 1700, 1900]  # X (Q(l/h))
N = [365, 361.6, 370.64, 379.68, 384.46, 395.5, 395.95, 397]  # Y (N(w))

# Definir la variable simbólica x que usaremos en el álgebra
x = symbols('x')

# Inicializamos una lista para almacenar los valores L_i(x)
L = []
# Calculamos los términos L_i(x) para cada valor de i (Cada punto)
for i in range(len(Q)):
    num = 1  # Numerador de L_i(x)
    den = 1  # Denominador de L_i(x)
    # Calculamos la productoria para el numerador y denominador
    for j in range(len(Q)):
        if i != j:  # Evitamos dividir entre 0
            num *= (x - Q[j])
            den *= (Q[i] - Q[j])
    # Calculamos L_i(x) y lo multiplicamos por el valor correspondiente de y_i
    L.append(N[i] * num / den)

# El polinomio es la suma de estos productos simbólicos
polynomial = sum(L)

# Mostramos el polinomio usando LaTeX sin expandir los productos
from IPython.display import display, Math

# Construimos manualmente el polinomio en LaTeX
latex_terms = []
n = len(Q)
for i in range(n):
    num_factors = []
    den_factors = []
    for j in range(n):
        if i != j:
            num_factors.append(f"(x-{Q[j]})")
            den_factors.append(f"({Q[i]}-{Q[j]})")
    num_str = ''.join(num_factors)
    den_str = ''.join(den_factors)
    term_latex = f"\\frac{{{num_str}}}{{{den_str}}}"
    latex_terms.append(f"{N[i]} \\times {term_latex}")

# Juntamos todos los términos
polynomial_latex = " + ".join(latex_terms)

# Mostramos el polinomio
display(Math('P(x) = ' + polynomial_latex))

# Generamos varios puntos cercanos para graficar
x_vals = np.linspace(min(Q), max(Q), 400)
# Evaluamos todos esos puntos cercanos con la función de interpolación
y_vals = [float(polynomial.subs(x, val)) for val in x_vals]

# Graficamos la curva
plt.plot(x_vals, y_vals, label='Polinomio de Interpolación', color='black')
# Graficamos los puntos conocidos originalmente
plt.scatter(Q, N, color='red', label='Puntos de Interpolación')
# Añadimos Etiquetas
plt.title('Interpolación de Lagrange')
plt.xlabel('Q(l/h)')
plt.ylabel('N(w)')
plt.legend()
plt.grid(True)
plt.show()