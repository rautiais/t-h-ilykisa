DROP TABLE IF EXISTS users CASCADE;
DROP TABLE IF EXISTS event_cat CASCADE;
DROP TABLE IF EXISTS events CASCADE;
DROP TABLE IF EXISTS groups CASCADE;
DROP TABLE IF EXISTS user_info CASCADE;


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

CREATE TABLE groups (
    id SERIAL PRIMARY KEY,
    group_name TEXT UNIQUE CHECK(group_name IS NOT NULL AND length(group_name) > 2),
    user_id INTEGER REFERENCES users
);

CREATE TABLE user_info (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users,
    group_id INTEGER REFERENCES groups,
    UNIQUE (user_id, group_id)
);