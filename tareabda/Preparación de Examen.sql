#1. Actores que tienen de primer nombre ‘Scarlett’.
SELECT actor_id, first_name, last_name FROM actor
WHERE first_name='SCARLETT';


#2. Actores que tienen de apellido ‘Johansson’.
SELECT actor_id, first_name, last_name FROM actor
WHERE last_name='JOHANSSON';


#3. Actores que contengan una ‘O’ en su nombre.
SELECT * FROM actor
WHERE FIRST_NAME LIKE "%o%";


#4. Actores que contengan una ‘O’ en su nombre y en una ‘A’ en su apellido.
SELECT first_name, last_name FROM actor
WHERE first_name LIKE "%o%" and last_name like "%a%";


#5. Ciudades que empiezan por ‘a’.
SELECT city_id, city FROM city
WHERE city LIKE "a%";

#6. Ciudades del country 61.
select co.country_id, c.city
from city as c
inner join country as co on c.country_id=co.country_id
where co.country_id='61';


#7. Ciudades del country ‘Spain’.
select co.country, c.city
from city as c
inner join country as co on c.country_id=co.country_id
where co.country='Spain';


#8. Peliculas con un rental_rate entre 1 y 3.
select title, rental_rate
from film
where rental_rate between '1' and '3';


#9. Película con menor duración.
select title, min(rental_duration) as duracion from film;


#10. Suma de rental_rate de todas las peliculas.
 select sum(rental_rate) as suma from film;
