/* 1. Количество исполнителей в каждом жанре. */
SELECT g.genre_name, COUNT(eg.executor_id)
FROM executors_genres AS eg
JOIN genres AS g ON eg.genre_id = g.genre_id
JOIN executors AS e ON eg.executor_id = e.executor_id
GROUP BY g.genre_id
ORDER BY g.genre_id;

/* 2. Количество треков, вошедших в альбомы 2019–2020 годов. */
SELECT a.album_name, a.release_date, COUNT(*)
FROM albums AS a
JOIN tracks AS t ON t.album_id = a.album_id
WHERE a.release_date BETWEEN '2019-01-01' AND '2020-12-31'
GROUP BY a.album_name, a.release_date
ORDER BY a.release_date;

/* 3. Средняя продолжительность треков по каждому альбому. */
SELECT a.album_name, ROUND(AVG(t.duration), 2)
FROM albums AS a
JOIN tracks AS t ON t.album_id = a.album_id
GROUP BY a.album_name
ORDER BY AVG(t.duration);

/* 4. Все исполнители, которые не выпустили альбомы в 2020 году. */
SELECT nickname
FROM executors
WHERE nickname <> (
	SELECT e.nickname
	FROM executors_albums AS ea
	JOIN albums AS a ON ea.album_id = a.album_id
	JOIN executors AS e ON ea.executor_id = e.executor_id
	WHERE a.release_date BETWEEN '2020-01-01' AND '2020-12-31'
	GROUP BY e.nickname
	ORDER BY e.nickname
	)
ORDER BY nickname;

/* 5. Названия сборников, в которых присутствует конкретный исполнитель (выберите его сами). */
SELECT c.collection_name
FROM collections AS c
JOIN collections_tracks AS ct ON c.collection_id = ct.collection_id
JOIN tracks AS t ON ct.track_id = t.track_id
JOIN albums AS a ON t.album_id = a.album_id
JOIN executors_albums AS ea ON a.album_id = ea.album_id
JOIN executors AS e ON ea.executor_id = e.executor_id
WHERE e.nickname = 'Баста'
GROUP BY c.collection_name;

/* 6. Названия альбомов, в которых присутствуют исполнители более чем одного жанра. */
SELECT a.album_name
FROM albums AS a
JOIN executors_albums AS ea ON a.album_id = ea.album_id
JOIN executors AS e ON ea.executor_id = e.executor_id
JOIN executors_genres AS eg ON e.executor_id = eg.executor_id
JOIN genres AS g ON eg.genre_id = g.genre_id
GROUP BY a.album_name
HAVING COUNT(g.genre_name) > 1
ORDER BY a.album_name;

/* 7. Наименования треков, которые не входят в сборники. */
SELECT t.track_name
FROM tracks AS t
LEFT JOIN collections_tracks AS ct ON t.track_id = ct.track_id
WHERE ct.collection_id IS NULL;

/* 8. Исполнитель или исполнители, написавшие самый короткий по продолжительности трек */
SELECT e.nickname
FROM executors e
JOIN executors_albums ea ON e.executor_id = ea.executor_id 
JOIN albums a ON ea.album_id = a.album_id 
JOIN tracks t ON a.album_id = t.album_id
WHERE t.duration = (
	SELECT MIN(duration)
	FROM tracks t2 
	)
GROUP BY e.nickname
ORDER BY e.nickname;

/* 9. Названия альбомов, содержащих наименьшее количество треков. */
SELECT a.album_name
FROM albums a 
JOIN tracks t ON a.album_id = t.album_id
GROUP BY a.album_name
HAVING COUNT(t.album_id) = (
	SELECT COUNT(*)
	FROM tracks t2 
	GROUP BY t2.album_id 
	ORDER BY COUNT(*)
	LIMIT 1
	);