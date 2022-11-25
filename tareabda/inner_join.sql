select c.city_id, c.city, co.country_id, co.country
from city as c
inner join country as co on c.country_id=co.country_id
where co.country='Angola';

select c.city_id, c.city, co.country_id, co.country
from city as c
inner join country as co on c.country_id=co.country_id
where c.city='Namibe';

select c.city_id, c.city, co.country_id, co.country
from city as c
inner join country as co on c.country_id=co.country_id
where c.country_id between '2' and '5';

