-- Creates the table unique_id with a unique id column that defaults to 1 if no value is provided
CREATE TABLE IF NOT EXISTS unique_id (
    id INT DEFAULT 1 UNIQUE,
    name VARCHAR(256)
);