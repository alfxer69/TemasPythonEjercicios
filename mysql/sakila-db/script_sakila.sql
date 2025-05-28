use sakila;
select * from film;

select count(*) as total_peliculas from film;
select count(*) as total_peliculas from film where replacement_cost>20;
select count(distinct rating) as tipos_rating from film; #nos da solo lo unico
select rating as tipos_rating,count(*) as total_by_rating from film group by rating;


select rating as tipo_de_rating,sum(replacement_cost) as costo_reemplazo_total from film group by rating;
select rating as tipo_de_rating,sum(rental_duration) as duracion_renta from film where rating='PG';
select rating,avg(length) as avg_duracion from film where rating='NC-17';
select rating,avg(rental_rate) as avg_rental_rate from film group by rating;
select min(length) as duracion_minima, max(length) as duracion_maxima from film;

select special_features as tipos_peliculas, min(length) as duracion_minima, max(length) as duracion_maxima from film group by special_features;
select rating as tipo_rating,min(rental_rate) as costo_minimo, max(rental_rate) as costo_maximo from film group by rating;
select rating as tipo_rating,min(replacement_cost) as min_cost_replace, max(replacement_cost) as max_cost_replace from film group by rating;

select release_year as año_lanzamiento, count(*) as release_year from film group by release_year;






 
