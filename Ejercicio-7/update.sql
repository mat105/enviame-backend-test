UPDATE
    employees e
    INNER JOIN countries cou ON (e.country_id = cou.id)
    INNER JOIN continents con ON (cou.continent_id = con.id)
SET
    e.salary = e.salary * (1 + con.anual_adjustment / 100)
WHERE
    e.salary <= 5000;