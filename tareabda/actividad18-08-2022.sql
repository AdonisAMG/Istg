-- Adonis Alexander Merchan Guadamud

/*Listar las categorias de peliculas, la cantidad de peliculas por categoria
y la duracion promedio
Utilizar las tablas film, film_category y category*/
SELECT name AS CATEGORIA, count(name) as cantidad_peliculas, avg(length) as duracion_promedio
FROM category
JOIN film_category USING(category_id)
JOIN film USING(film_id)
GROUP BY category.category_id;

/*Mostrar el listado del pago total realizado por cada cliente utilizando el siguiente formato
nombre cliente,apellido cliente, monto total de pagos
Utilizar la tabla payment y customer*/
select CONCAT(first_name," ",last_name) as nombre_apellido, amount as monto_pagos
from customer, payment
WHERE payment.payment_id = customer.customer_id;