import random

# Función para calcular la probabilidad
def probabilidad(num_lanzamientos):
    # Simular los lanzamientos de la moneda
    resultados = [random.choice([0, 1]) for _ in range(num_lanzamientos)]  # 0 = cruz, 1 = cara

    # Calcular la probabilidad de obtener el número de caras
    prob = resultados.count(1) / num_lanzamientos
    return prob 

# Ejemplo de uso
num_lanzamientos = 10
prob = probabilidad(num_lanzamientos)

print(f"La probabilidad de obtener cara en {num_lanzamientos} lanzamientos es {prob:.4f}")
