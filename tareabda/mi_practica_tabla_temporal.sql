#1. Actores que tienen de primer nombre ‘Scarlett’.
SELECT * FROM actor;
CREATE TEMPORARY TABLE Nombre_Scarlett
	SELECT actor_id, first_name, last_name
	FROM actor WHERE first_name='SCARLETT';
SELECT * FROM Nombre_Scarlett;



CREATE TEMPORARY TABLE IF NOT EXISTS scarlett_actor AS(SELECT *FROM actor);
SELECT *FROM  scarlett_actor;

SELECT * FROM city;
CREATE TEMPORARY TABLE Nombre_citys SELECT city FROM city WHERE city LIKE  '%s';
SELECT * FROM Nombre_citys;


drop table scarlett_actor;