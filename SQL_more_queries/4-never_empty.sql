-- Creates the table id_not_null with id defaulting to 1 if no value is provided
CREATE TABLE IF NOT EXISTS id_not_null (id INT DEFAULT 1, name VARCHAR(256));