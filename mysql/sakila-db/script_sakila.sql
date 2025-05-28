use sakila;
select * from film;
select count(*) as total_peliculas from film;
select count(*) as total_peliculas from film where replacement_cost>20;

