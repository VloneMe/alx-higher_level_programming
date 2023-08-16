-- SQL: script that creates the table id_not_null.
-- 	If the table id_not_null already exists, the script won't fail
CREATE TABLE IF NOT EXISTS id_not_null (
    id INT DEFAULT 1,
    name VARCHAR(256)
);
