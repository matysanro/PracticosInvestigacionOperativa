# Programa para maximizar el beneficio de la construcción de casas tipo A y B

from scipy.optimize import linprog

# Coeficientes de la función objetivo (negativos porque linprog minimiza)
# 40,000 por casa A y 30,000 por casa B
c = [-40000, -30000]

# Restricciones
# Cada fila representa una restricción: [coeficiente de A, coeficiente de B]
A = [
    [3, 2],  # 3x + 2y <= 180  (Presupuesto máximo)
    [1, 1]   # x + y <= 80     (Máximo total de casas)
]

# Lado derecho de las restricciones
b = [180, 80]

# Límites para las variables: no pueden ser negativas
x_bounds = (0, None)
y_bounds = (0, None)

# Resolver el problema usando linprog
res = linprog(c, A_ub=A, b_ub=b, bounds=[x_bounds, y_bounds], method="highs")

# Mostrar resultados
if res.success:
    print("=== RESULTADO ÓPTIMO ===")
    print(f"Cantidad óptima de casas tipo A: {res.x[0]:.2f}")
    print(f"Cantidad óptima de casas tipo B: {res.x[1]:.2f}")
    beneficio_total = -res.fun
    print(f"Beneficio máximo: €{beneficio_total:.2f}")
else:
    print("No se pudo encontrar una solución óptima.")
