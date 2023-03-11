CREATE TABLE IF NOT EXISTS genres (
	genre_id SERIAL PRIMARY KEY,
	genre_name VARCHAR(20) NOT NULL
);

CREATE TABLE IF NOT EXISTS executors (
	executor_id SERIAL PRIMARY KEY,
	nickname VARCHAR(20) NOT NULL
);

CREATE TABLE IF NOT EXISTS executors_genres (
	executor_id INTEGER REFERENCES executors (executor_id),
	genre_id INTEGER REFERENCES genres (genre_id),
	CONSTRAINT pk PRIMARY KEY (executor_id, genre_id)
);

CREATE TABLE IF NOT EXISTS albums (
	album_id SERIAL PRIMARY KEY,
	album_name VARCHAR(20) NOT NULL,
	release_date DATE NOT NULL
);

CREATE TABLE IF NOT EXISTS executors_albums (
	album_id INTEGER REFERENCES albums (album_id),
	executor_id INTEGER REFERENCES executors (executor_id),
	CONSTRAINT pk_executors_albums PRIMARY KEY (album_id, executor_id)
);

CREATE TABLE IF NOT EXISTS tracks (
	track_id SERIAL PRIMARY KEY,
	track_name VARCHAR(20) NOT NULL,
	duration INTEGER NOT NULL,
	album_id INTEGER REFERENCES albums (album_id)
);

CREATE TABLE IF NOT EXISTS collections (
	collection_id SERIAL PRIMARY KEY,
	collection_name VARCHAR(20) NOT NULL,
	release_date DATE NOT NULL
);

CREATE TABLE IF NOT EXISTS collections_tracks (
	collection_id INTEGER REFERENCES collections (collection_id),
	track_id INTEGER REFERENCES tracks (track_id),
	CONSTRAINT pk_collections_tracks PRIMARY KEY (collection_id, track_id)
);