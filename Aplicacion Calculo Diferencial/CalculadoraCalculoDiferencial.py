import sympy as sp
import matplotlib.pyplot as plt
import numpy as np

def ingresar_funcion():
    x = sp.symbols('x')
    func = sp.sympify(input('Ingresa la función en términos de x (por ejemplo, 3*x**2): '))
    return func, x

def calcular_derivada(func, x):
    derivada = sp.diff(func, x)
    return derivada

def graficar_funcion(func, x):
    f = sp.lambdify(x, func, 'numpy')
    x_vals = np.linspace(-10, 10, 100)
    y_vals = f(x_vals)
    plt.plot(x_vals, y_vals, label=f'Función: {func}')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.legend()
    plt.grid(True)
    plt.show()
    
def graficar_derivada(derivada, x):
    d = sp.lambdify(x, derivada, 'numpy')
    x_vals = np.linspace(-10, 10, 100)
    y_vals = d(x_vals)
    plt.plot(x_vals, y_vals, label=f'Derivada: {derivada}', color='r')
    plt.xlabel('x')
    plt.ylabel("f'(x)")
    plt.legend()
    plt.grid(True)
    plt.show()

def main():
    func, x = ingresar_funcion()
    derivada = calcular_derivada(func, x)
    print(f'Función: {func}')
    print(f'Derivada: {derivada}')
    
    graficar_funcion(func, x)
    graficar_derivada(derivada, x)

if __name__ == '__main__':
    main()
