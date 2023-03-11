SELECT album_name, release_date
FROM albums
WHERE release_date BETWEEN '2018-01-01' AND '2018-12-31';

SELECT track_name, duration
FROM tracks
ORDER BY duration DESC
LIMIT 1;

SELECT track_name
FROM tracks
WHERE duration >= 210;

SELECT collection_name
FROM collections
WHERE release_date BETWEEN '2018-01-01' AND '2020-12-31';

SELECT nickname
FROM executors
WHERE nickname NOT LIKE '% %';

SELECT track_name
FROM tracks
WHERE track_name LIKE '%мой%' OR track_name LIKE '%my%'