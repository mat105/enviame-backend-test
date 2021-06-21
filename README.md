# Test desafio backend ENVIAME

## Requisitios

Para poder correr los ejercicios 3, 4, 5 y 6 se necesita tener instalado python (se desarrolló con python 3.9).


## Ejercicio 1 y 2

Realizados en Python 3.9 + Django.

Para correrlos ejecutar:

    docker-compose build
    docker-compose up -d

Entrar al container web y ejecutar:

    python manage.py migrate

La api esta en:

localhost:8000/companies/

La empresa se compone de estos campos:
- name (string)
- address (string)
- tax_id (string)
- country (string (3 letras))
- phone (string)

Se puede agregar empresas al azar corriendo:

    python manage.py filldb --companies=40

Puede correr tests de get, post, put, patch, delete con:

    python manage.py test

## Ejercicio 3
    python main.py

Podrá ver todos los palindromos encontrados (sin repetir) y el string convertido a otro donde los palindromos estan en mayuscula para verlos.

## Ejercicio 4
    pip install requests
    python consumir.py

Se generara un archivo donde se guarda el resultado del request.

*No pude probar un estado OK (200), porque arroja que el "carrier_code" es incorrecto*

## Ejercicio 5
    python fibo.py

Mostrará cual es el primer numero de la serie de fibonacci con más de 1000 divisores.

## Ejercicio 6
    python estimar.py

Creará 20 distancias al azar y calculará el rango y el tiempo de envío.

## Ejercicio 7
Puede ejecutarse el SQL en un SQLFIDDLE (o en una base propia si se tiene un motor instalado) y probar como queda la tabla antes y después del update siguiendo el SQL dentro de la carpeta Ejercicio-7.
