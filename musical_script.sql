DROP TABLE IF EXISTS
	executor,
	genre,
	executor_genre,
	album,
	executor_album,
	track,
	collection,
	track_collection;

CREATE TABLE IF NOT EXISTS executor (
	executor_id SERIAL      PRIMARY KEY,
	nickname    VARCHAR(30) NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS genre (
	genre_id   SERIAL      PRIMARY KEY,
	genre_name VARCHAR(30) NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS executor_genre (
	executor_id INTEGER REFERENCES executor (executor_id),
	genre_id    INTEGER REFERENCES genre (genre_id),
	CONSTRAINT pk_executor_genre
	PRIMARY KEY (executor_id, genre_id)
);

CREATE TABLE IF NOT EXISTS album (
	album_id     SERIAL      PRIMARY KEY,
	album_name   VARCHAR(30) NOT NULL,
	release_date DATE        NOT NULL
	             CONSTRAINT album_release_date_range
	             CHECK(release_date BETWEEN '1900-01-01' AND CURRENT_DATE)
);

CREATE TABLE IF NOT EXISTS executor_album (
	executor_id INTEGER REFERENCES executor (executor_id),
	album_id    INTEGER REFERENCES album (album_id),
	CONSTRAINT pk_executor_album
	PRIMARY KEY (executor_id, album_id)
);

CREATE TABLE IF NOT EXISTS track (
	track_id   SERIAL      PRIMARY KEY,
	track_name VARCHAR(30) NOT NULL,
	duration   INTEGER     NOT NULL
               CONSTRAINT duration_range
               CHECK(duration >= 5),
	album_id   INTEGER     REFERENCES album (album_id)
);

CREATE TABLE IF NOT EXISTS collection (
	collection_id   SERIAL      PRIMARY KEY,
	collection_name VARCHAR(30) NOT NULL,
	release_date    DATE        NOT NULL
	                CONSTRAINT collection_release_date_range
	                CHECK(release_date BETWEEN '1900-01-01' AND CURRENT_DATE)
);

CREATE TABLE IF NOT EXISTS track_collection (
	track_id      INTEGER REFERENCES track (track_id),
	collection_id INTEGER REFERENCES collection (collection_id),
	CONSTRAINT pk_track_collection
	PRIMARY KEY (track_id, collection_id)
);