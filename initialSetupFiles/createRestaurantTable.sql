DROP TABLE IF EXISTS flight_data_restaurants;

CREATE TABLE flight_data_restaurants AS 
    SELECT a23 as name, a47 as address, a62 as city, a66 as stars from tempyelp
        WHERE POSITION(lower('restaurant') in lower(a10)) > 0;

ALTER TABLE flight_data_restaurants
    ALTER COLUMN stars TYPE numeric(2,1) USING stars::numeric;
