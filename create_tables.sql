-- Exported from QuickDBD: https://www.quickdatabasediagrams.com/
-- Link to schema: https://app.quickdatabasediagrams.com/#/d/5ktCGG
-- NOTE! If you have used non-SQL datatypes in your design, you will have to change these here.

-- Drop the 'movie' table if it already exists.
DROP TABLE IF EXISTS movie CASCADE;

CREATE TABLE "movie" (
    "id" int NOT NULL,
    "title" varchar NOT NULL,
    "tagline" varchar,
    "overview" varchar,
    "homepage" varchar,
    "release_date" date NOT NULL,
    "budget" money NOT NULL,
    "revenue" money NOT NULL,
    "popularity" float NOT NULL,
    "runtime" int NOT NULL,
    "poster_path" varchar,
    PRIMARY KEY (id)
);

-- Drop the 'actor' table if it already exists.
DROP TABLE IF EXISTS actor;

-- Actors and the movies in which they starred.
CREATE TABLE "actor" (
	"id" int NOT NULL,
    "actor_id" int NOT NULL,
    "name" varchar NOT NULL,
    "profile_path" varchar,
    "movie_id" int NOT NULL,
    "character" varchar,
	PRIMARY KEY (id),
    FOREIGN KEY (movie_id) REFERENCES movie(id)
);

-- Drop the 'director' table if it already exists.
DROP TABLE IF EXISTS director;

-- Directors and movies that they directed.
CREATE TABLE "director" (
	"id" int NOT NULL,
    "director_id" int NOT NULL,
    "name" varchar NOT NULL,
    "profile_path" varchar,
    "movie_id" int NOT NULL,
	PRIMARY KEY (id),
    FOREIGN KEY (movie_id) REFERENCES movie(id)
);