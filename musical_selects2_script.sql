/* 1. Количество исполнителей в каждом жанре. */
  SELECT g.genre_name, COUNT(eg.executor_id) AS "Количество исполнителей"
    FROM genre AS g 
         JOIN executor_genre AS eg 
         ON g.genre_id = eg.genre_id 
GROUP BY g.genre_name
ORDER BY COUNT(eg.executor_id)

/* 2. Количество треков, вошедших в альбомы 2019–2020 годов. */
SELECT COUNT(*) AS "Всего исполнителей"
  FROM track AS t
       JOIN album AS a 
       ON t.album_id = a.album_id 
 WHERE DATE_PART('year', a.release_date) IN (2019, 2020)

/* 3. Средняя продолжительность треков по каждому альбому. */
  SELECT a.album_name, ROUND(AVG(t.duration), 2) AS "Средняя продолжительность"
    FROM album AS a
		 JOIN track AS t 
		 ON t.album_id = a.album_id
GROUP BY a.album_name
ORDER BY AVG(t.duration);

/* 4. Все исполнители, которые не выпустили альбомы в 2020 году. */
  SELECT nickname
    FROM executor
   WHERE nickname <> (
		   SELECT DISTINCT e.nickname
		     FROM executor_album AS ea
		 		  JOIN album AS a
		 		  ON ea.album_id = a.album_id
		 		  
		 		  JOIN executor AS e 
		 		  ON ea.executor_id = e.executor_id
		    WHERE DATE_PART('year', a.release_date) = 2020
		 )
ORDER BY nickname;

/* 5. Названия сборников, в которых присутствует конкретный исполнитель (выберите его сами). */
SELECT DISTINCT c.collection_name
  FROM collection AS c
	   JOIN track_collection AS tc 
	   ON c.collection_id = tc.collection_id
	   
	   JOIN track AS t 
	   ON tc.track_id = t.track_id
	   
	   JOIN album AS a 
	   ON t.album_id = a.album_id
	   
	   JOIN executor_album AS ea 
	   ON a.album_id = ea.album_id
	   
	   JOIN executor AS e 
	   ON ea.executor_id = e.executor_id
  WHERE e.nickname = 'Баста';

/* 6. Названия альбомов, в которых присутствуют исполнители более чем одного жанра. */
  SELECT DISTINCT a.album_name
    FROM album AS a
		 JOIN executor_album AS ea 
		 ON a.album_id = ea.album_id
		 
		 JOIN executor AS e 
		 ON ea.executor_id = e.executor_id
		 
		 JOIN executor_genre AS eg 
		 ON e.executor_id = eg.executor_id
		 
		 JOIN genre AS g 
		 ON eg.genre_id = g.genre_id
GROUP BY a.album_name, e.executor_id
  HAVING COUNT(g.genre_name) > 1
ORDER BY a.album_name;

/* 7. Наименования треков, которые не входят в сборники. */
SELECT t.track_name
  FROM track AS t
	   LEFT JOIN track_collection AS tc 
	   ON t.track_id = tc.track_id
 WHERE tc.collection_id IS NULL;

/* 8. Исполнитель или исполнители, написавшие самый короткий по продолжительности трек */
  SELECT e.nickname
    FROM executor e
		 JOIN executor_album AS ea 
		 ON e.executor_id = ea.executor_id 
		 
		 JOIN album AS a 
		 ON ea.album_id = a.album_id 
		 
		 JOIN track AS t 
		 ON a.album_id = t.album_id
   WHERE t.duration = (
		 SELECT MIN(duration)
		   FROM track
		 )
GROUP BY e.nickname
ORDER BY e.nickname;

/* 9. Названия альбомов, содержащих наименьшее количество треков. */
  SELECT a.album_name
    FROM album AS a 
		 JOIN track AS t 
		 ON a.album_id = t.album_id
GROUP BY a.album_name
  HAVING COUNT(t.album_id) = (
		   SELECT COUNT(*)
		     FROM track
		 GROUP BY album_id 
		 ORDER BY COUNT(*)
		    LIMIT 1
		 );