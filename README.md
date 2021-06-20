# Test desafio backend ENVIAME


## Ejercicio 1 y 2
    docker-compose build
    docker-compose up -d

Entrar al container web y ejecutar:

    python manage.py migrate

La api esta en:

localhost:8000/companies/

Se puede agregar empresas al azar corriendo:

    python manage.py filldb --companies=40

Puede correr tests de get, post, put, patch, delete con:

    python manage.py test

## Ejercicio 3
    python main.py

Podrá ver todos los palindromos encontrados (sin repetir) y el string convertido a otro donde los palindromos estan en mayuscula para verlos.

## Ejercicio 4
    python consumir.py

Se generara un archivo donde se guarda el resultado del request.
No pude probar un estado OK, porque arroja que el carrier_code es incorrecto

## Ejercicio 5
    python fibo.py

Mostrará cual es el primer numero de la serie de fibonacci con más de 1000 divisores.

## Ejercicio 6
    python estimar.py

Creará 20 distancias al azar y calculará el rango y el tiempo de envío.

## Ejercicio 7
Puede ejecutarse el SQL en un SQLFIDDLE y probar como quedaría el update corriendo el siguiente select antes:

    SELECT e.*, con.anual_adjustment, IF(e.salary <= 5000, e.salary * (1 + con.anual_adjustment / 100), e.salary) AS ajustado FROM employees e INNER JOIN countries cou ON (e.country_id = cou.id) INNER JOIN continents con ON (cou.continent_id = con.id);
