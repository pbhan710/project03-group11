-- Exported from QuickDBD: https://www.quickdatabasediagrams.com/
-- Link to schema: https://app.quickdatabasediagrams.com/#/d/5ktCGG
-- NOTE! If you have used non-SQL datatypes in your design, you will have to change these here.

-- Modify this code to update the DB schema diagram.
-- To reset the sample schema, replace everything with
-- two dots ('..' - without quotes).

CREATE TABLE "movie" (
    "id" int   NOT NULL,
    "title" varchar   NOT NULL,
    "tagline" varchar   NOT NULL,
    "overview" varchar   NOT NULL,
    "homepage" varchar   NOT NULL,
    "release_date" date   NOT NULL,
    "budget" money   NOT NULL,
    "revenue" money   NOT NULL,
    "popularity" float   NOT NULL,
    "runtime" int   NOT NULL,
    "poster_path" varchar   NOT NULL,
    CONSTRAINT "pk_movie" PRIMARY KEY (
        "id"
     )
);

-- Actors and the movies in which they starred.
CREATE TABLE "actor" (
    "id" int   NOT NULL,
    "name" varchar   NOT NULL,
    "character" varchar   NOT NULL,
    "profile_path" varchar   NOT NULL
);

-- Directors and movies for which they directed.
CREATE TABLE "director" (
    "id" int   NOT NULL,
    "name" varchar   NOT NULL,
    "profile_path" varchar   NOT NULL
);

ALTER TABLE "actor" ADD CONSTRAINT "fk_actor_id" FOREIGN KEY("id")
REFERENCES "movie" ("id");

ALTER TABLE "director" ADD CONSTRAINT "fk_director_id" FOREIGN KEY("id")
REFERENCES "movie" ("id");

