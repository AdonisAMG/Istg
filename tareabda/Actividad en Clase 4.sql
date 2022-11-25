	#En la tabla categoria
select * from category;
 #1. Mostrar la cantidad de categorias 
SELECT COUNT(category_id) AS cantidad_categorias
FROM category
WHERE category_id;
 
 #2. Mostrar las categorias que empiecen con la letra c
SELECT name AS categoria_inicia_c
FROM category
WHERE name LIKE "C%";

 #3. Mostrar las categorias que contengan una letra t
 SELECT name AS categoria_con_t
FROM category
WHERE name LIKE "%t%";
 
 
	#En la tabla country
select * from country;

#4. Mostrar la cantidad de paises que terminen con la letra a
SELECT COUNT(country) AS pais_termina_letra_a
FROM country
WHERE country LIKE "%t";

#5. Mostrar los paises que empiecen con la silaba Un 
SELECT country AS pais_empieza_un
FROM country
WHERE country LIKE "un%";

#6. Mostrar los paises que no contengan la letra e
SELECT country AS pais_sin_e
FROM country
WHERE country NOT LIKE "%E%";
