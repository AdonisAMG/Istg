/*UNIDAD 2 - TABLAS TEMPORALES Y VISTAS*/

SELECT * FROM FILM;

SELECT TITLE,DESCRIPTION, REPLACEMENT_COST
FROM FILM WHERE REPLACEMENT_COST>20;



CREATE TEMPORARY TABLE PELICULAS_COSTO_R20
	SELECT TITLE,DESCRIPTION, REPLACEMENT_COST
	FROM FILM WHERE REPLACEMENT_COST>20;
    
SELECT * FROM PELICULAS_COSTO_R20;



CREATE OR REPLACE VIEW V_PELICULAS_COSTO_R20 AS
	SELECT TITLE,DESCRIPTION, REPLACEMENT_COST
	FROM FILM WHERE REPLACEMENT_COST>20;
    
SELECT * FROM V_PELICULAS_COSTO_R20;