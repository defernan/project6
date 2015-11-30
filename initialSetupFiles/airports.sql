DROP TABLE IF EXISTS janelson.airports;

CREATE TABLE tmp (
    id integer,
    name text,
    city text,
    country text,
    faa text,
    icao text,
    latitude text,
    longitude text,
    altitude text,
    timezone text,
    dst text,
    a text
);

\copy tmp from ./airports.csv delimiter ',' csv;

CREATE TABLE janelson.airports AS SELECT id, name, city, country FROM tmp;
DROP TABLE tmp;
