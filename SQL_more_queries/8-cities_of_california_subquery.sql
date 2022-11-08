--  script that lists all the cities of California that can be found in the database hbtn_0d_usa
SELECT cities.id, cities.name FROM cities, states WHERE states.id = (SELECT states.id FROM states WHERE state.name = "California") ORDER BY cities.id ASC;
