import random

# Guardar el resultado de calculos previos para evitar recursiones muy grandes a medida que voy creciendo.
memo = [0, 1, 1]

# Fibonacci pero con la primer posicion siendo 0
def fibonacci(n):
    if len(memo) <= n:
        res = fibonacci(n-1) + fibonacci(n-2)
        memo.append(res)
        return res
    else:
        return memo[n]

def estimar_entrega(distancia):
    rango = distancia // 100
    return fibonacci(rango), rango


distancias = sorted([random.randint(0, 2000) for x in range(20)])

for distancia in distancias:
    dias, rango = estimar_entrega(distancia)
    print(f'El tiempo de entrega para una distancia de {distancia}km con rango {rango} es {dias} dias')
