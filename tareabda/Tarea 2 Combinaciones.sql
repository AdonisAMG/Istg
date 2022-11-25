/*1.      
Visualiza los 10 actores que
han participado en más películas*/
select CONCAT(first_name," ",last_name) as ACTOR
		, count(actor.actor_id) as CANTIDAD_PELICULAS
from actor,film_actor,film
where actor.actor_id = film_actor.actor_id
and film.film_id = film_actor.film_id
group by actor.actor_id
order by CANTIDAD_PELICULAS desc limit 10;

/*2.      
Visualiza los clientes de países
que empiezan con S*/
select  first_name, country
from country co, city c, address a, customer cu
where co.country_id = c.city_id and c.city_id=a.city_id and a.address_id=cu.customer_id
and country like "s%";

/*3.      
Visualiza el top 10 de países con
más clientes*/
select country.country, count(country) as numero_clientes
from city
inner join country
on city.country_id=country.country_id
inner join address 
on address.address_id=city.city_id
inner join customer 
on customer.address_id=address.address_id
group by country
order by numero_clientes desc limit 10;

/*4.      
Mostrar todas las películas que
ha alquilado el cliente Deborah Walker*/
select CONCAT(first_name," ",last_name) as cliente, count(inventory_id) as numero_pelis, rental_date as dia_rentado
from rental, customer
where rental.rental_id=customer.customer_id
AND first_name = 'Deborah'
AND last_name = 'Walker'
GROUP BY first_name, last_name;


