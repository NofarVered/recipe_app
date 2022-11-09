CREATE DATABASE IF NOT EXISTS recipes;
use recipes;

CREATE TABLE IF NOT EXISTS Ingrediant(
    name VARCHAR(12) PRIMARY KEY,
    has_gluten BOOLEAN,
    has_dairy BOOLEAN
);