DROP TABLE IF EXISTS Users;

CREATE TABLE users (
    id SERIAL PRIMARY KEY, 
    username TEXT UNIQUE,
    password TEXT
);