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
    event_cat_name TEXT UNIQUE CHECK(event_cat_name IS NOT NULL AND length(event_cat_name) > 2 AND length(event_cat_name) < 35)
);

CREATE TABLE IF NOT EXISTS events (
    id SERIAL PRIMARY KEY,
    event_name TEXT UNIQUE CHECK(event_name IS NOT NULL AND length(event_name) > 2 AND length(event_name) < 35),
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

INSERT INTO event_cat (event_cat_name) VALUES ('Falling down');
INSERT INTO event_cat (event_cat_name) VALUES ('Tripping');
INSERT INTO event_cat (event_cat_name) VALUES ('Dropping something');
INSERT INTO event_cat (event_cat_name) VALUES ('Bump into something');
INSERT INTO event_cat (event_cat_name) VALUES ('Breaking something');
INSERT INTO event_cat (event_cat_name) VALUES ('Injuring yourself');
INSERT INTO events (event_name, event_cat_id, points) VALUES ('Falling down the stairs', '1', '45');
INSERT INTO events (event_name, event_cat_id, points) VALUES ('Falling down while standing', '1', '55');
INSERT INTO events (event_name, event_cat_id, points) VALUES ('Tripping while walking', '2', '15');
INSERT INTO events (event_name, event_cat_id, points) VALUES ('Dropping your phone', '3', '20');
INSERT INTO events (event_name, event_cat_id, points) VALUES ('Dropping a drink', '3', '25');
INSERT INTO events (event_name, event_cat_id, points) VALUES ('Hit a wall', '4', '50');
INSERT INTO events (event_name, event_cat_id, points) VALUES ('Breaking your phone', '5', '75');
INSERT INTO events (event_name, event_cat_id, points) VALUES ('Twisting your ankle', '6', '90');
INSERT INTO events (event_name, event_cat_id, points) VALUES ('Getting a bruise', '6', '30');