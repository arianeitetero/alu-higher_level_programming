-- Task 8: List cities of California using subquery
-- Select cities where state name is California
SELECT id, name FROM cities
WHERE state_id = (
  SELECT id FROM states WHERE name = 'California'
)
ORDER BY id ASC;

