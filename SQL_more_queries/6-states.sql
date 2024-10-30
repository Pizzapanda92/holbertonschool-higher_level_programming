-- Creates the database hbtn_0d_usa if it does not already exist
CREATE DATABASE if not EXISTS hbtn_0d_usa;
-- Use the database hbtn_0d_usa
USE hbtn_0d_usa;
-- Creates the table states with an auto-increment primary key and a not-null name column
CREATE TABLE IF NOT EXISTS states (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(256) NOT NULL
);