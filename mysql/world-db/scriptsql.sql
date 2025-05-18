use world;
select Name, Continent from country;
select Name ,Population from country where Continent='Europe';
select Name from city order by Name;
select Name from country limit 5;

select Name,Population from country
where Continent='Asia' and Population>=10000000;
