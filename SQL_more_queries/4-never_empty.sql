-- Task 4: Create id_not_null table with default id value
-- Create table id_not_null
CREATE TABLE IF NOT EXISTS id_not_null (
  id INT DEFAULT 1,
  name VARCHAR(256)
);

