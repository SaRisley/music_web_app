-- First, we must delete (drop) all our tables
DROP TABLE IF EXISTS artists;
DROP SEQUENCE IF EXISTS artists_id_seq;

-- Then, we recreate them
CREATE SEQUENCE IF NOT EXISTS albums_id_seq;
CREATE TABLE artists (
    id SERIAL PRIMARY KEY,
    artist text,
    genre text
);

-- Finally, we add any records that are needed for the tests to run
INSERT INTO artists (artist, genre) VALUES ('Pixies', 'Rock');
INSERT INTO artists (artist, genre) VALUES ('ABBA', 'Pop');
INSERT INTO artists (artist, genre) VALUES ('Taylor Swift', 'Pop');
INSERT INTO artists (artist, genre) VALUES ('Nina Simone', 'Jazz');