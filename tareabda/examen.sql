SELECT  count(title) AS titulo
FROM film
where description like "%crocodile%" and description like "%shark%";


SELECT  last_name, count(last_name) as numer_apellido
FROM actor
group by last_name
order by numer_apellido desc;