DROP TABLE IF EXISTS users CASCADE;
DROP TABLE IF EXISTS event_cat CASCADE;
DROP TABLE IF EXISTS events CASCADE;
DROP TABLE IF EXISTS groups CASCADE;
DROP TABLE IF EXISTS user_info CASCADE;


CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY, 
    username TEXT UNIQUE CHECK(username IS NOT NULL AND length(username) > 2 AND length(username) < 20),
    password TEXT CHECK (password IS NOT NULL AND length(password) > 7)
);

CREATE TABLE IF NOT EXISTS events (
    id SERIAL PRIMARY KEY,
    event_name TEXT UNIQUE CHECK(event_name IS NOT NULL AND length(event_name) > 2 AND length(event_name) < 20)
);

CREATE TABLE IF NOT EXISTS event_cat (
    id SERIAL PRIMARY KEY,
    event_cat_name TEXT UNIQUE CHECK(event_cat_name IS NOT NULL AND length(event_cat_name) > 2 AND length(event_cat_name) < 20),
    events_id INTEGER REFERENCES events
);

CREATE TABLE IF NOT EXISTS groups (
    id SERIAL PRIMARY KEY,
    member_id INTEGER REFERENCES users,
    group_name TEXT UNIQUE CHECK(group_name IS NOT NULL AND length(group_name) > 2 AND length(group_name) < 20)
);

CREATE TABLE IF NOT EXISTS user_info (
    id SERIAL PRIMARY KEY,
    username INTEGER REFERENCES users,
    group_id INTEGER REFERENCES groups,
    user_id INTEGER REFERENCES users,
    UNIQUE (user_id, group_id)
);