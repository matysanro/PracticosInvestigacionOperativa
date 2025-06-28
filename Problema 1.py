# Programa para maximizar los ingresos de las revistas

from scipy.optimize import linprog

# Coeficientes de la función objetivo (negativos porque linprog minimiza)
c = [-3, -5]

# Restricciones
A = [
    [1, 1],   # x + y <= 250 (cartuchos negros)
    [1, 2]    # x + 2y <= 500 (cartuchos color)
]

b = [250, 500]

# Límites de las variables
x_bounds = (0, None)
y_bounds = (0, None)

# Resolver el problema
res = linprog(c, A_ub=A, b_ub=b, bounds=[x_bounds, y_bounds], method="highs")

# Mostrar resultados
if res.success:
    print("=== RESULTADO ÓPTIMO ===")
    print(f"Cantidad de revistas deportivas: {res.x[0]:.2f}")
    print(f"Cantidad de revistas culturales: {res.x[1]:.2f}")
    ingreso_total = -res.fun
    print(f"Ingreso máximo: €{ingreso_total:.2f}")
else:
    print("No se pudo encontrar una solución óptima.")
