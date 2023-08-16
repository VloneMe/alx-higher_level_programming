-- SQL: Script that creates the table unique_id on your MySQL server.
-- 	If the table unique_id already exists, the script won't fail
CREATE TABLE IF NOT EXISTS unique_id (
    id INT DEFAULT 1 UNIQUE,
    name VARCHAR(256)
);
