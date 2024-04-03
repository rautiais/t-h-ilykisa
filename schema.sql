DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS event_cat;
DROP TABLE IF EXISTS events;

CREATE TABLE users (
    id SERIAL PRIMARY KEY, 
    username TEXT UNIQUE CHECK(username IS NOT NULL AND length(username) > 2),
    password TEXT CHECK (password IS NOT NULL AND length(password) > 7)
);

CREATE TABLE events (
    id SERIAL PRIMARY KEY,
    event_name TEXT UNIQUE CHECK(event_name IS NOT NULL AND length(event_name) > 2)
);

CREATE TABLE event_cat (
    id SERIAL PRIMARY KEY,
    event_cat_name TEXT UNIQUE CHECK(event_cat_name IS NOT NULL AND length(event_cat_name) > 2),
    events_id INTEGER REFERENCES events
);