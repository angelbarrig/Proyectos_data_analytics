-- 1. Crea el esquema de la BBDD.
CREATE SCHEMA IF NOT EXISTS public;

-- 2. Muestra los nombres de todas las películas con una clasificación por edades de 'R'.
SELECT title FROM film WHERE rating = 'R';

-- 3. Encuentra los nombres de los actores que tengan un "actor_id" entre 30 y 40.
SELECT first_name, last_name FROM actor WHERE actor_id BETWEEN 30 AND 40;

-- 4. Obtén las películas cuyo idioma coincide con el idioma original.
SELECT title FROM film WHERE language_id = original_language_id;

-- 5. Ordena las películas por duración de forma ascendente.
SELECT title, length FROM film ORDER BY length ASC;

-- 6. Encuentra el nombre y apellido de los actores que tengan 'Allen' en su apellido.
SELECT first_name, last_name FROM actor WHERE last_name ILIKE '%Allen%';

-- 7. Cantidad total de películas en cada clasificación de la tabla "film".
SELECT rating, COUNT(*) AS total_peliculas FROM film GROUP BY rating;

-- 8. Título de todas las películas que son 'PG-13' o tienen una duración mayor a 3 horas.
SELECT title FROM film WHERE rating = 'PG-13' OR length > 180;

-- 9. Encuentra la variabilidad de lo que costaría reemplazar las películas.
SELECT VARIANCE(replacement_cost) AS varianza_reemplazo FROM film;

-- 10. Mayor y menor duración de una película de nuestra BBDD.
SELECT MAX(length) AS max_duracion, MIN(length) AS min_duracion FROM film;

-- 11. Encuentra lo que costó el antepenúltimo alquiler ordenado por día.
SELECT amount FROM payment ORDER BY payment_date DESC OFFSET 2 LIMIT 1;

-- 12. Título de las películas que no sean ni 'NC-17' ni 'G' en su clasificación.
SELECT title FROM film WHERE rating NOT IN ('NC-17', 'G');

-- 13. Promedio de duración de las películas para cada clasificación.
SELECT rating, AVG(length) AS promedio_duracion FROM film GROUP BY rating;

-- 14. Título de todas las películas que tengan una duración mayor a 180 minutos.
SELECT title FROM film WHERE length > 180;

-- 15. ¿Cuánto dinero ha generado en total la empresa?
SELECT SUM(amount) AS total_generado FROM payment;

-- 16. Muestra los 10 clientes con mayor valor de id.
SELECT * FROM customer ORDER BY customer_id DESC LIMIT 10;

-- 17. Nombre y apellido de los actores que aparecen en la película con título 'Egg Igby'.
SELECT a.first_name, a.last_name 
FROM actor a 
JOIN film_actor fa ON a.actor_id = fa.actor_id 
JOIN film f ON fa.film_id = f.film_id 
WHERE f.title ILIKE 'Egg Igby';

-- 18. Selecciona todos los nombres de las películas únicos.
SELECT DISTINCT title FROM film;

-- 19. Título de las películas que son comedias y tienen una duración mayor a 180 minutos.
SELECT f.title 
FROM film f 
JOIN film_category fc ON f.film_id = fc.film_id 
JOIN category c ON fc.category_id = c.category_id 
WHERE c.name = 'Comedy' AND f.length > 180;

-- 20. Categorías de películas que tienen un promedio de duración superior a 110 minutos.
SELECT c.name, AVG(f.length) AS promedio_duracion 
FROM category c 
JOIN film_category fc ON c.category_id = fc.category_id 
JOIN film f ON fc.film_id = f.film_id 
GROUP BY c.name 
HAVING AVG(f.length) > 110;

-- 21. ¿Cuál es la media de duración del alquiler de las películas?
SELECT AVG(return_date - rental_date) AS media_duracion_alquiler FROM rental;

-- 22. Crea una columna con el nombre y apellidos de todos los actores y actrices.
SELECT CONCAT(first_name, ' ', last_name) AS nombre_completo FROM actor;

-- 23. Números de alquiler por día, ordenados por cantidad de alquiler descendente.
SELECT DATE(rental_date) AS dia, COUNT(*) AS cantidad_alquileres 
FROM rental 
GROUP BY DATE(rental_date) 
ORDER BY cantidad_alquileres DESC;

-- 24. Encuentra las películas con una duración superior al promedio.
SELECT title, length 
FROM film 
WHERE length > (SELECT AVG(length) FROM film);

-- 25. Averigua el número de alquileres registrados por mes.
SELECT TO_CHAR(rental_date, 'YYYY-MM') AS mes, COUNT(*) AS cantidad 
FROM rental 
GROUP BY TO_CHAR(rental_date, 'YYYY-MM') 
ORDER BY mes;

-- 26. Encuentra el promedio, la desviación estándar y varianza del total pagado.
SELECT AVG(amount) AS promedio, STDDEV(amount) AS desviacion_estandar, VARIANCE(amount) AS varianza 
FROM payment;

-- 27. ¿Qué películas se alquilan por encima del precio medio?
SELECT title, rental_rate 
FROM film 
WHERE rental_rate > (SELECT AVG(rental_rate) FROM film);

-- 28. Muestra el id de los actores que hayan participado en más de 40 películas.
SELECT actor_id 
FROM film_actor 
GROUP BY actor_id 
HAVING COUNT(film_id) > 40;

-- 29. Obtener todas las películas y, si están disponibles, mostrar la cantidad disponible.
SELECT f.title, COUNT(i.inventory_id) AS cantidad_disponible 
FROM film f 
LEFT JOIN inventory i ON f.film_id = i.film_id 
GROUP BY f.title;

-- 30. Obtener los actores y el número de películas en las que ha actuado.
SELECT a.first_name, a.last_name, COUNT(fa.film_id) AS numero_peliculas 
FROM actor a 
JOIN film_actor fa ON a.actor_id = fa.actor_id 
GROUP BY a.actor_id, a.first_name, a.last_name;

-- 31. Películas y actores que han actuado en ellas, incluso si no tienen actores asociados.
SELECT f.title, a.first_name, a.last_name 
FROM film f 
LEFT JOIN film_actor fa ON f.film_id = fa.film_id 
LEFT JOIN actor a ON fa.actor_id = a.actor_id;

-- 32. Todos los actores y películas en las que han actuado, incluso si no han actuado en ninguna.
SELECT a.first_name, a.last_name, f.title 
FROM actor a 
LEFT JOIN film_actor fa ON a.actor_id = fa.actor_id 
LEFT JOIN film f ON fa.film_id = f.film_id;

-- 33. Obtener todas las películas que tenemos y todos los registros de alquiler.
SELECT f.title, r.rental_id, r.rental_date 
FROM film f 
LEFT JOIN inventory i ON f.film_id = i.film_id 
LEFT JOIN rental r ON i.inventory_id = r.inventory_id;

-- 34. Encuentra los 5 clientes que más dinero se hayan gastado con nosotros.
SELECT c.first_name, c.last_name, SUM(p.amount) AS total_gastado 
FROM customer c 
JOIN payment p ON c.customer_id = p.customer_id 
GROUP BY c.customer_id 
ORDER BY total_gastado DESC 
LIMIT 5;

-- 35. Selecciona todos los actores cuyo primer nombre es 'Johnny'.
SELECT * FROM actor WHERE first_name ILIKE 'Johnny';

-- 36. Renombra la columna "first_name" como Nombre y "last_name" como Apellido.
SELECT first_name AS Nombre, last_name AS Apellido FROM actor;

-- 37. Encuentra el ID del actor más bajo y más alto en la tabla actor.
SELECT MIN(actor_id) AS id_minimo, MAX(actor_id) AS id_maximo FROM actor;

-- 38. Cuenta cuántos actores hay en la tabla "actor".
SELECT COUNT(*) AS total_actores FROM actor;

-- 39. Selecciona todos los actores y ordénalos por apellido en orden ascendente.
SELECT * FROM actor ORDER BY last_name ASC;

-- 40. Selecciona las primeras 5 películas de la tabla "film".
SELECT * FROM film LIMIT 5;

-- 41. Agrupa los actores por su nombre y cuenta cuántos tienen el mismo nombre.
SELECT first_name, COUNT(*) AS repeticiones 
FROM actor 
GROUP BY first_name 
ORDER BY repeticiones DESC;
-- (El nombre más repetido será el que aparezca en la primera fila de la consulta anterior).

-- 42. Encuentra todos los alquileres y los nombres de los clientes que los realizaron.
SELECT r.rental_id, c.first_name, c.last_name 
FROM rental r 
JOIN customer c ON r.customer_id = c.customer_id;

-- 43. Muestra todos los clientes y sus alquileres si existen, incluyendo los que no tienen.
SELECT c.first_name, c.last_name, r.rental_id 
FROM customer c 
LEFT JOIN rental r ON c.customer_id = r.customer_id;

-- 44. Realiza un CROSS JOIN entre las tablas film y category.
SELECT * FROM film CROSS JOIN category;
/* 
¿Aporta valor esta consulta? ¿Por qué? 
Respuesta: No, no aporta valor analítico ni práctico. Un CROSS JOIN genera un "producto cartesiano",
lo que significa que une cada película existente con TODAS las categorías existentes sin importar a qué
categoría pertenece realmente la película en la base de datos.
*/

-- 45. Encuentra los actores que han participado en películas de la categoría 'Action'.
SELECT DISTINCT a.first_name, a.last_name 
FROM actor a 
JOIN film_actor fa ON a.actor_id = fa.actor_id 
JOIN film_category fc ON fa.film_id = fc.film_id 
JOIN category c ON fc.category_id = c.category_id 
WHERE c.name = 'Action';

-- 46. Encuentra todos los actores que no han participado en películas.
SELECT a.first_name, a.last_name 
FROM actor a 
LEFT JOIN film_actor fa ON a.actor_id = fa.actor_id 
WHERE fa.film_id IS NULL;

-- 47. Selecciona el nombre de los actores y la cantidad de películas en las que han participado.
SELECT a.first_name, a.last_name, COUNT(fa.film_id) AS cantidad_peliculas 
FROM actor a 
JOIN film_actor fa ON a.actor_id = fa.actor_id 
GROUP BY a.actor_id;

-- 48. Crea una vista llamada "actor_num_peliculas".
CREATE OR REPLACE VIEW actor_num_peliculas AS 
SELECT a.first_name, a.last_name, COUNT(fa.film_id) AS numero_peliculas 
FROM actor a 
JOIN film_actor fa ON a.actor_id = fa.actor_id 
GROUP BY a.actor_id;

-- 49. Calcula el número total de alquileres realizados por cada cliente.
SELECT customer_id, COUNT(rental_id) AS total_alquileres 
FROM rental 
GROUP BY customer_id;

-- 50. Calcula la duración total de las películas en la categoría 'Action'.
SELECT SUM(f.length) AS duracion_total 
FROM film f 
JOIN film_category fc ON f.film_id = fc.film_id 
JOIN category c ON fc.category_id = c.category_id 
WHERE c.name = 'Action';

-- 51. Crea una tabla temporal "cliente_rentas_temporal".
CREATE TEMPORARY TABLE cliente_rentas_temporal AS 
SELECT customer_id, COUNT(rental_id) AS total_alquileres 
FROM rental 
GROUP BY customer_id;

-- 52. Crea una tabla temporal "peliculas_alquiladas" (alquiladas al menos 10 veces).
CREATE TEMPORARY TABLE peliculas_alquiladas AS 
SELECT f.title, COUNT(r.rental_id) AS veces_alquilada 
FROM film f 
JOIN inventory i ON f.film_id = i.film_id 
JOIN rental r ON i.inventory_id = r.inventory_id 
GROUP BY f.film_id 
HAVING COUNT(r.rental_id) >= 10;

-- 53. Películas alquiladas por 'Tammy Sanders' y que aún no se han devuelto. 
SELECT f.title 
FROM film f 
JOIN inventory i ON f.film_id = i.film_id 
JOIN rental r ON i.inventory_id = r.inventory_id 
JOIN customer c ON r.customer_id = c.customer_id 
WHERE c.first_name ILIKE 'Tammy' AND c.last_name ILIKE 'Sanders' AND r.return_date IS NULL 
ORDER BY f.title ASC;

-- 54. Actores que han actuado en al menos una película 'Sci-Fi' (orden apellido).
SELECT DISTINCT a.first_name, a.last_name 
FROM actor a 
JOIN film_actor fa ON a.actor_id = fa.actor_id 
JOIN film_category fc ON fa.film_id = fc.film_id 
JOIN category c ON fc.category_id = c.category_id 
WHERE c.name = 'Sci-Fi' 
ORDER BY a.last_name ASC;

-- 55. Actores en películas alquiladas después de la primera vez que se alquiló 'Spartacus Cheaper'.
SELECT DISTINCT a.first_name, a.last_name 
FROM actor a 
JOIN film_actor fa ON a.actor_id = fa.actor_id 
JOIN film f ON fa.film_id = f.film_id 
JOIN inventory i ON f.film_id = i.film_id 
JOIN rental r ON i.inventory_id = r.inventory_id 
WHERE r.rental_date > (
    SELECT MIN(r2.rental_date) 
    FROM rental r2 
    JOIN inventory i2 ON r2.inventory_id = i2.inventory_id 
    JOIN film f2 ON i2.film_id = f2.film_id 
    WHERE f2.title ILIKE 'Spartacus Cheaper'
) 
ORDER BY a.last_name ASC;

-- 56. Actores que no han actuado en ninguna película de la categoría 'Music'.
SELECT a.first_name, a.last_name 
FROM actor a 
WHERE a.actor_id NOT IN (
    SELECT fa.actor_id 
    FROM film_actor fa 
    JOIN film_category fc ON fa.film_id = fc.film_id 
    JOIN category c ON fc.category_id = c.category_id 
    WHERE c.name = 'Music'
);

-- 57. Encuentra el título de todas las películas que fueron alquiladas por más de 8 días.
SELECT DISTINCT f.title 
FROM film f 
JOIN inventory i ON f.film_id = i.film_id 
JOIN rental r ON i.inventory_id = r.inventory_id 
WHERE (r.return_date - r.rental_date) > INTERVAL '8 days';

-- 58. Encuentra el título de todas las películas que son de la misma categoría que 'Animation'.
SELECT f.title 
FROM film f 
JOIN film_category fc ON f.film_id = fc.film_id 
JOIN category c ON fc.category_id = c.category_id 
WHERE c.name = 'Animation';

-- 59. Películas que tienen la misma duración que 'Dancing Fever'.
SELECT title 
FROM film 
WHERE length = (SELECT length FROM film WHERE title ILIKE 'Dancing Fever') 
  AND title NOT ILIKE 'Dancing Fever' 
ORDER BY title ASC;

-- 60. Clientes que han alquilado al menos 7 películas distintas.
SELECT c.first_name, c.last_name 
FROM customer c 
JOIN rental r ON c.customer_id = r.customer_id 
JOIN inventory i ON r.inventory_id = i.inventory_id 
GROUP BY c.customer_id 
HAVING COUNT(DISTINCT i.film_id) >= 7 
ORDER BY c.last_name ASC;

-- 61. Cantidad total de películas alquiladas por categoría.
SELECT c.name, COUNT(r.rental_id) AS total_alquileres 
FROM category c 
JOIN film_category fc ON c.category_id = fc.category_id 
JOIN inventory i ON fc.film_id = i.film_id 
JOIN rental r ON i.inventory_id = r.inventory_id 
GROUP BY c.name;

-- 62. Encuentra el número de películas por categoría estrenadas en 2006.
SELECT c.name, COUNT(f.film_id) AS numero_peliculas 
FROM category c 
JOIN film_category fc ON c.category_id = fc.category_id 
JOIN film f ON fc.film_id = f.film_id 
WHERE f.release_year = 2006 
GROUP BY c.name;

-- 63. Obtén todas las combinaciones posibles de trabajadores con las tiendas que tenemos.
SELECT s.first_name, s.last_name, st.store_id 
FROM staff s 
CROSS JOIN store st;

-- 64. Cantidad total de películas alquiladas por cada cliente.
SELECT c.customer_id, c.first_name, c.last_name, COUNT(r.rental_id) AS peliculas_alquiladas 
FROM customer c 
JOIN rental r ON c.customer_id = r.customer_id 
GROUP BY c.customer_id, c.first_name, c.last_name;