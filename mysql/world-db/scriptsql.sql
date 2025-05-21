use world;
select Name, Continent from country;
select Name ,Population from country where Continent='Europe';
select Name from city order by Name;
select Name from country limit 5;

select Name,Population from country
where Continent='Asia' and Population>=10000000;

select Name, Population from city
order by CountryCode asc, Population desc;

select Name, IndepYear from country
where IndepYear between 1900 and 2000;

select Name as 'Nombre del Pais', (Population/10000000) 
as 'Poblacion (millones)' from country;

select Name, (GNP/Population) as 'GNP per capita' from country
where Population>0;

select Name from city where Name like 'New%';

select Name from country where IndepYear is null;

select Name from city where CountryCode in 
(select Code from country where Continent='Europe');

select Name,Continent from country where LifeExpectancy>=75 and Population>20000000;

select Name as 'Pais',(GNP/Population) as 'Per Capita',Continent as 'Continente' from country where Population>0 order by Population desc;

select Name as 'Ciudad' from city where Name like 'lima%';

select Name from city where CountryCode in 
(select Code from country where Continent='Europe');

select Name as 'Pais' from country where Code in (select CountryCode from countrylanguage);

select * from countrylanguage;

select * from city;

select * from country;

select Name as 'Pais' from country where Code in (select CountryCode from countrylanguage); 

select c.Name as 'Pais', cl.Language as 'Idioma', cl.Percentage
from country c join countrylanguage cl on c.Code=cl.CountryCode;






