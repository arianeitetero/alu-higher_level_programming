-- Task 5: Create unique_id table with UNIQUE id
-- Create table unique_id
CREATE TABLE IF NOT EXISTS unique_id (
  id INT DEFAULT 1 UNIQUE,
  name VARCHAR(256)
);

