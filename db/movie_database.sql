DROP TABLE IF EXISTS movies;
DROP TABLE IF EXISTS movie_casts;
DROP TABLE IF EXISTS movie_genres;
DROP TABLE IF EXISTS actors;
DROP TABLE IF EXISTS genres;
DROP TABLE IF EXISTS directors;
CREATE TABLE directors (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    age INT,
    bio text
);
CREATE TABLE genres (id SERIAL PRIMARY KEY, type VARCHAR(255));
CREATE TABLE actors (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    age INT,
    bio text
);
CREATE TABLE movie_genres (
    id SERIAL PRIMARY KEY,
    genre1 INT REFERENCES genres(id) ON DELETE CASCADE,
    genre2 INT REFERENCES genres(id) ON DELETE CASCADE
);
CREATE TABLE movie_casts (
    id SERIAL PRIMARY KEY,
    actor1 INT REFERENCES actors(id) ON DELETE CASCADE,
    actor2 INT REFERENCES actors(id) ON DELETE CASCADE,
    actor3 INT REFERENCES actors(id) ON DELETE CASCADE
);
CREATE TABLE movies (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255),
    year INT,
    description text,
    cast_id INT REFERENCES movie_casts(id) ON DELETE CASCADE,
    genre_id INT REFERENCES movie_genres(id) ON DELETE CASCADE,
    director_id INT REFERENCES directors(id) ON DELETE CASCADE
);
-- INSERT INTO genres (type)
-- VALUES ('Crime');
-- INSERT INTO genres (type)
-- VALUES ('Action');
-- INSERT INTO genres (type)
-- VALUES ('Horror');
-- INSERT INTO genres (type)
-- VALUES ('Drama');
-- INSERT INTO genres (type)
-- VALUES ('Thriller');
-- INSERT INTO genres (type)
-- VALUES ('Western');
-- INSERT INTO genres (type)
-- VALUES ('Science Fiction');
-- INSERT INTO genres (type)
-- VALUES ('Comedy');
-- INSERT INTO genres (type)
-- VALUES ('Romance');
-- INSERT INTO genres (type)
-- VALUES ('Adventure');
-- INSERT INTO genres (type)
-- VALUES ('Noir');
-- INSERT INTO genres (type)
-- VALUES ('Animation');
-- INSERT INTO genres (type)
-- VALUES ('Fantasy');
-- INSERT INTO directors (name, age, bio)
-- VALUES (
--         'Quentin Tarantino',
--         59,
--         'Quentin Jerome Tarantino March 27, 1963 is an American film director, writer, producer, and actor. His films are characterized by frequent references to popular culture and film genres, non-linear storylines, dark humor, stylized violence, extended dialogue, pervasive use of profanity, cameos and ensemble casts.'
--     );
-- INSERT INTO actors (name, age, bio)
-- VALUES (
--         'John Travolta',
--         69,
--         'John Joseph Travolta (born February 18, 1954)[1][2] is an American actor. He came to public attention during the 1970s, appearing on the television sitcom Welcome Back, Kotter (1975–1979) and starring in the box office successes Carrie (1976), Saturday Night Fever (1977), Grease (1978), and Urban Cowboy (1980)'
--     );
-- INSERT INTO actors (name, age, bio)
-- VALUES (
--         'Samuel L. Jackson',
--         74,
--         'Samuel Leroy Jackson (born December 21, 1948) is an American actor and producer. One of the most widely recognized actors of his generation, the films in which he has appeared have collectively grossed over $27 billion worldwide, making him the second highest-grossing actor of all time.'
--     );
-- INSERT INTO actors (name, age, bio)
-- VALUES (
--         'Uma Thurman',
--         52,
--         'Uma Karuna Thurman (born April 29, 1970) is an American actress and former model. She has performed in a variety of films, from romantic comedies and dramas to science fiction and action films.'
--     );
-- INSERT INTO movie_casts(actor1, actor2, actor3)
-- VALUES (1, 2, 3);
-- INSERT INTO movie_genres(genre1, genre2)
-- VALUES(1, 5);
-- INSERT INTO movies (
--         title,
--         year,
--         description,
--         cast_id,
--         genre_id,
--         director_id
--     )
-- VALUES (
--         'Pulp Fiction',
--         1994,
--         'Pulp Fiction is a 1994 American crime film written and directed by Quentin Tarantino, who conceived it with Roger Avary.',
--         1,
--         1,
--         1
--     );