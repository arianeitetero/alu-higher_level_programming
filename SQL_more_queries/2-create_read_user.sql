-- Task 2: Create database hbtn_0d_2 and read-only user user_0d_2
-- Create database
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
-- Create user user_0d_2
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
-- Grant SELECT only
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';

