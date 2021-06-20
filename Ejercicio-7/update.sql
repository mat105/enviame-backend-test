-- Actualizar los sueldos de los empleados que ganen $5000 o menos, de acuerdo al reajuste anual del continente al que pertenecen.

CREATE TABLE countries ( id int(10) unsigned NOT NULL AUTO_INCREMENT, continent_id int(11) NOT NULL, name varchar(25) NOT NULL, PRIMARY KEY (id) );
CREATE TABLE continents ( id int(10) unsigned NOT NULL AUTO_INCREMENT, name varchar(25) NOT NULL, anual_adjustment int(11) NOT NULL, PRIMARY KEY (id) );
CREATE TABLE employees ( id int(10) unsigned NOT NULL AUTO_INCREMENT, country_id int(11) NOT NULL, first_name varchar(25) NOT NULL, last_name varchar(25) NOT NULL, salary int(11) NOT NULL, PRIMARY KEY (id) );

INSERT INTO continents values (null, 'América', 4); INSERT INTO continents values (null, 'Europa', 5); INSERT INTO continents values (null, 'Asia', 6); INSERT INTO continents values (null, 'Oceanía', 6); INSERT INTO continents values (null, 'Africa', 5);
INSERT INTO countries values (null, 1, 'Chile'); INSERT INTO countries values (null, 1, 'Argentina'); INSERT INTO countries values (null, 1, 'Canadá'); INSERT INTO countries values (null, 1, 'Colombia'); INSERT INTO countries values (null, 2, 'Alemania'); INSERT INTO countries values (null, 2, 'Francia'); INSERT INTO countries values (null, 2, 'España'); INSERT INTO countries values (null, 2, 'Grecia'); INSERT INTO countries values (null, 3, 'India'); INSERT INTO countries values (null, 3, 'Japón'); INSERT INTO countries values (null, 3, 'Corea del Sur'); INSERT INTO countries values (null, 4, 'Australia');
INSERT INTO employees values (null, 1, 'Pedro', 'Rojas', 2000); INSERT INTO employees values (null, 2, 'Luciano', 'Alessandri', 2100); INSERT INTO employees values (null, 3, 'John', 'Carter', 3050); INSERT INTO employees values (null, 4, 'Alejandra', 'Benavides', 2150); INSERT INTO employees values (null, 5, 'Moritz', 'Baring', 6000); INSERT INTO employees values (null, 6, 'Thierry', 'Henry', 5900); INSERT INTO employees values (null, 7, 'Sergio', 'Ramos', 6200); INSERT INTO employees values (null, 8, 'Nikoleta', 'Kyriakopulu', 7000); INSERT INTO employees values (null, 9, 'Aamir', 'Khan', 2000); INSERT INTO employees values (null, 10, 'Takumi', 'Fujiwara', 5000); INSERT INTO employees values (null, 11, 'Heung-min', 'Son', 5100); INSERT INTO employees values (null, 12, 'Peter', 'Johnson', 6100);

-- Ejercicio.

-- VER COMO QUEDARÍA
SELECT
    e.*,
    con.anual_adjustment,
    IF(
        e.salary <= 5000,
        e.salary * (1 + con.anual_adjustment / 100),
        e.salary
    ) AS ajustado
FROM
    employees e
    INNER JOIN countries cou ON (e.country_id = cou.id)
    INNER JOIN continents con ON (cou.continent_id = con.id);

-- UPDATE
UPDATE
    employees e
    INNER JOIN countries cou ON (e.country_id = cou.id)
    INNER JOIN continents con ON (cou.continent_id = con.id)
SET
    e.salary = e.salary * (1 + con.anual_adjustment / 100)
WHERE
    e.salary <= 5000;

-- VERIFICAR EL UPDATE
SELECT
    e.*,
    con.anual_adjustment
FROM
    employees e
    INNER JOIN countries cou ON (e.country_id = cou.id)
    INNER JOIN continents con ON (cou.continent_id = con.id);
