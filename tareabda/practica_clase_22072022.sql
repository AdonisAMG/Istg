/*CONSULTAS MULTITABLA*/

SELECT COUNT(*)
FROM ACTOR, FILM, FILM_ACTOR
WHERE ACTOR.ACTOR_ID = FILM_ACTOR.ACTOR_ID
AND FILM.FILM_ID = FILM_ACTOR.FILM_ID
AND FIRST_NAME LIKE "PENELOPE" AND LAST_NAME LIKE"GUINESS";

SELECT COUNT(*)
FROM ACTOR
JOIN FILM_ACTOR USING(ACTOR_ID)
JOIN FILM USING(FILM_ID)
WHERE FIRST_NAME LIKE "PENELOPE" AND LAST_NAME LIKE"GUINESS";


/* LISTADO DE ACTORES Y LA CANTIDAD DE PELICULAS EN LAS QUE ACTUARON*/
SELECT CONCAT(first_name," ",last_name) AS ACTOR
		, count(actor.actor_id) AS CANTIDAD_PELICULAS
FROM actor,film_actor,film
WHERE actor.actor_id = film_actor.actor_id
AND film.film_id = film_actor.film_id
GROUP BY actor.actor_id;


SELECT CONCAT(first_name," ",last_name) AS ACTOR, 
count(actor.actor_id) AS CANTIDAD_PELICULAS
FROM actor
JOIN film_actor USING(actor_id)
JOIN film USING (film_id)
GROUP BY actor.actor_id
ORDER BY CANTIDAD_PELICULAS DESC;

/*film - film_category, category TITLE, NAME*/
SELECT title AS PELICULA, name AS CATEGORIA
FROM film,film_category,category
WHERE film.film_id = film_category.film_id
AND category.category_id = film_category.category_id;

/*PELICULAS CON SU RESPECTIVA CATEGORIA*/
SELECT name AS CATEGORIA, COUNT(film.film_id) AS CANTIDAD_PELICULAS
FROM category
JOIN film_category USING(category_id)
JOIN film USING(film_id)
GROUP BY category.category_id;


/*  MOSTRAR LAS CIUDADES CON SUS RESPECTIVOS PAISES
CITY Y COUNTRY CIUDAD PAIS  */
select c.city as ciudad, co.country as pais
from city as c
inner join country as co 
on c.country_id=co.country_id;

select city, country
from city, country
WHERE city.city_id = country.country_id;


/*MOSTRAR LA CANTIDAD DE CIUDADES REGISTRADAS POR PAIS*/
select count(city.city) as Ciudades , country.country as pais 
from country
join city using (country_id)
group by city.country_id;

select country.country, count(city.city)
from country
join city using (country_id)
GROUP BY country.country_id;

/*Mostrar el country, la ciudad y dirección de cada customer.
COUNTRY, CITY, ADDRESS , CUSTOMER*/
select country, city, address, first_name
from country co, city c, address a, customer cu
where co.country_id = c.city_id and c.city_id=a.city_id and a.address_id=cu.customer_id;



select country.country, city.city, address.address, customer.first_name, customer.last_name
from  city as ciudad, customer as cliente 
join country using(country)
join city using(city)
join customer using(address_id)
group by customer.address_id;

