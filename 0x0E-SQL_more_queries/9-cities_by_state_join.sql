-- Script to list all cities contained in the database hbtn_0d_usa

-- Select the city ID, city name, and state name
SELECT cities.id, cities.name, states.name
FROM cities
JOIN states ON cities.state_id = states.id
ORDER BY cities.id ASC;
