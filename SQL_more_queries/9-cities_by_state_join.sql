-- Task 9: List cities and their states using JOIN
-- Select city and state names
SELECT cities.id, cities.name, states.name FROM cities, states
WHERE cities.state_id = states.id
ORDER BY cities.id ASC;

