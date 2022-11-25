SELECT COUNT(LAST_NAME) AS CANTIDAD_APELLIDOS, last_name as apellido
FROM actor	
group by last_name;