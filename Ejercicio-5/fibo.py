# Guardar el resultado de calculos previos para evitar recursiones muy grandes a medida que voy creciendo.
memo = [1, 1]


def fibo(n):
    if len(memo) <= n:
        res = fibo(n-1) + fibo(n-2)
        memo.append(res)
        return res
    else:
        return memo[n]


# Se siguen la teoria de:
# http://aula.educa.aragon.es/datos/espad/MateTecno/bloque1/Unidad02/pagina_18.html
# Realizar la descomposicion factorial del numero en numeros primos. Luego sumar 1 a sus potencias y multiplicarlas.
def minimo_divisor(n):
    # Si es multiplo de 2, el menor es 2
    if (n % 2 == 0):
        return 2

    # Iterar desde 3 hasta la raiz cuadrada de n. Se usa raiz porque un numero no primo tiene si o si un divisor primo menor a su raiz cuadrada
    # Si la descomposicion factorial contase con dos numeros primos mayores a la raiz no se cumpliria que su multiplicacion diese N (sino un numero mayor)
    i = 3
    while(i * i <= n):
        if (n % i == 0):
            return i
        i += 2 # Aumentar de a 2 ya que filtre los pares

    # Si el numero es primo devolver a el mismo
    return n


# Obtener la cantidad de divisores de un numero
def contar_divisores(n):
    fac = {}

    while n > 1:
        dm = minimo_divisor(n)
        if dm in fac:
            fac[dm] += 1
        else:
            fac[dm] = 1
        n/=dm

    resultado = 1
    potencias = fac.values()
    for pot in potencias:
        resultado *= (pot+1)

    return resultado


def buscar_fibonacci_1000_divisores():
    i = 0
    divs = 0
    loop = True

    while loop:
        fib = fibo(i)
        divs = contar_divisores(fib)
        if divs >= 1000:
            loop = False
            i = fib
        else:
            i+=1

    return i, divs


res = buscar_fibonacci_1000_divisores()
print(f"El primer numero de la serie de fibonacci con mas de 1000 divisores es: {res[0]} y tiene {res[1]} divisores")
