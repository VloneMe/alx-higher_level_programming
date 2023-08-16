-- SQL: Script that creates the database hbtn_0d_usa and the table states
--	(in the database hbtn_0d_usa) on your MySQL server.
-- 	If the database hbtn_0d_usa or table states already exist, the script won't fail
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;

CREATE TABLE IF NOT EXISTS states (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(256) NOT NULL
);
