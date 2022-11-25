/*Requiere ver un listado de las categorías de películas, cuantas veces 
se han rentado películas de cada categoría y el ingreso total que ha 
generado cada una de estas categorías en la tienda.*/

SELECT c.name, count(r.inventory_id) as inventario, sum(p.amount) as ingresos
FROM category c, film f, film_category fc, rental r, customer cus, address a, inventory i,payment p
WHERE c.category_id = fc.category_id
AND f.film_id = fc.film_id
AND r.customer_id = cus.customer_id
AND cus.address_id = a.address_id
AND r.inventory_id = i.inventory_id
AND i.film_id = f.film_id
AND p.rental_id = r.rental_id
group by c.category_id;


/*Requiere ver el listado de las ventas totales que ha generado cada 
una de las tiendas y su respectivo administrador.*/

SELECT se.store_id, sum(p.amount) as ingresos, 
concat(sf.first_name," ",sf.last_name) as encargado_da
FROM film f, film_category fc, rental r, customer cus, address a, inventory i,payment p, staff sf, store se
WHERE f.film_id = fc.film_id
AND r.customer_id = cus.customer_id
AND cus.address_id = a.address_id
AND r.inventory_id = i.inventory_id
AND i.film_id = f.film_id
AND p.rental_id = r.rental_id
AND sf.store_id=se.store_id
group by sf.first_name;

