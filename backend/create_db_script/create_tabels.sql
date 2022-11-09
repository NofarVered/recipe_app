CREATE DATABASE IF NOT EXISTS recipes;
use recipes;

CREATE TABLE IF NOT EXISTS Ingrediant(
    name VARCHAR(12) PRIMARY KEY,
    free_gluten BOOLEAN,
    free_dairy BOOLEAN
);