CREATE DATABASE IF NOT EXISTS recipes;
use recipes;

CREATE TABLE IF NOT EXISTS Ingrediant(
    name VARCHAR(12) PRIMARY KEY,
    gluten_free BOOLEAN,
    dairy_free BOOLEAN
);