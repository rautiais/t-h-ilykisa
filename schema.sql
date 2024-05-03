DROP TABLE IF EXISTS users CASCADE;
DROP TABLE IF EXISTS events CASCADE;
DROP TABLE IF EXISTS event_cat CASCADE;
DROP TABLE IF EXISTS groups CASCADE;
DROP TABLE IF EXISTS user_info CASCADE;
DROP TABLE IF EXISTS user_events CASCADE;

CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY, 
    username TEXT UNIQUE CHECK(username IS NOT NULL AND length(username) > 2 AND length(username) < 20),
    password TEXT CHECK (password IS NOT NULL AND length(password) > 7)
);

CREATE TABLE IF NOT EXISTS event_cat (
    id SERIAL PRIMARY KEY,
    event_cat_name TEXT UNIQUE CHECK(event_cat_name IS NOT NULL AND length(event_cat_name) > 2 AND length(event_cat_name) < 25)
);

CREATE TABLE IF NOT EXISTS events (
    id SERIAL PRIMARY KEY,
    event_name TEXT UNIQUE CHECK(event_name IS NOT NULL AND length(event_name) > 2 AND length(event_name) < 25),
    event_cat_id INTEGER REFERENCES event_cat(id),
    points INTEGER CHECK (points > 0)
);

CREATE TABLE IF NOT EXISTS groups (
    id SERIAL PRIMARY KEY,
    member_id INTEGER REFERENCES users,
    group_name TEXT UNIQUE CHECK(group_name IS NOT NULL AND length(group_name) > 2 AND length(group_name) < 20),
    total_points INTEGER DEFAULT 0
);

CREATE TABLE IF NOT EXISTS user_info (
    id SERIAL PRIMARY KEY,
    username INTEGER REFERENCES users,
    user_id INTEGER REFERENCES users(id),
    group_id INTEGER REFERENCES groups(id),
    UNIQUE (user_id, group_id)
);

CREATE TABLE IF NOT EXISTS user_events (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(id),
    group_id INTEGER REFERENCES groups(id),
    event_id INTEGER REFERENCES events(id),
    points INTEGER,
    date_logged TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);