#CREACIÓN DE TABLAS TEMPORALES
#1. Actores que tienen de primer nombre ‘Scarlett’.
#2. Actores que contengan una ‘O’ en su nombre.
#3. Ciudades que acaban por ‘s’.

#1. Actores que tienen de primer nombre ‘Scarlett’.
SELECT * FROM actor;
CREATE TEMPORARY TABLE Nombre_Scarlett
	SELECT actor_id, first_name, last_name
	FROM actor WHERE first_name='SCARLETT';
SELECT * FROM Nombre_Scarlett;

#2. Actores que contengan una ‘O’ en su nombre.
SELECT * FROM actor;
CREATE TEMPORARY TABLE letra_o_en_nombre
	SELECT actor_id, first_name
	FROM actor WHERE first_name like "%O%";
SELECT * FROM letra_o_en_nombre;

#3. Ciudades que acaban por ‘s’.
SELECT * FROM city;
CREATE TEMPORARY TABLE ciudad_acaba_s
	SELECT city_id, city
	FROM city WHERE city like "%s";
SELECT * FROM ciudad_acaba_s;


#CREACIÓN DE VISTAS
#4. Películas con una duración entre 80 y 100.
#5. Ciudades tiene el country ‘Spain’
#6. Películas con un titulo de más de 12 letras.

#4. Películas con una duración entre 80 y 100.
SELECT * FROM FILM;
CREATE OR REPLACE VIEW duracion_entre_80_100 AS
	SELECT TITLE, DESCRIPTION, length
	FROM FILM WHERE length>=80 and length<=100;
SELECT * FROM duracion_entre_80_100;

#5. Ciudades tiene el country ‘Spain’
SELECT * FROM city;
SELECT * FROM country;
CREATE OR REPLACE VIEW ciudades_españa AS
	SELECT city.city, country.country
	FROM city, country where city.country_id=country.country_id AND country ='Spain';
SELECT * FROM ciudades_españa;

#6. Películas con un titulo de más de 12 letras.
SELECT * FROM FILM;
CREATE OR REPLACE VIEW titulo_mas_12_letras AS
	SELECT film_id, title
	FROM FILM WHERE length(title)>12;
SELECT * FROM titulo_mas_12_letras;
