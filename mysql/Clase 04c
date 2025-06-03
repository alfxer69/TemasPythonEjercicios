use sakila;
select * from film;

select rating, 
	special_features as caract_especiales,
    count(*) as total_peliculas,
    avg(length) as duracion,
    sum(replacement_cost) as costo_reemplazo
    from film 
    group by rating,special_features
    order by rating,special_features;

select rating,
	special_features as caract_especial,
    count(*) as duracion_renta,
    avg(rental_rate) as prom_costo_renta,
    sum(replacement_cost) as costo_reemplazo
    from film 
    group by rating,special_features
    order by rating,special_features desc;
    
    
    
    


	