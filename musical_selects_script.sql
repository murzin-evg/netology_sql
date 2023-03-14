SELECT album_name, release_date
  FROM album
 WHERE DATE_PART('year', release_date) = 2018;

  SELECT track_name, duration
    FROM track
ORDER BY duration DESC
   LIMIT 1;

SELECT track_name
  FROM track
 WHERE duration >= 210;

SELECT collection_name
  FROM collection
 WHERE DATE_PART('year', release_date) in (2018, 2019, 2020);

SELECT nickname
  FROM executor
 WHERE nickname NOT LIKE '% %';

SELECT track_name
  FROM track
 WHERE track_name LIKE '%мой%' OR track_name LIKE '%my%';

/* Тесты с датами*/
SELECT album_name, release_date
  FROM album
 WHERE DATE_PART('month', release_date) = 09;

SELECT album_name, release_date
  FROM album
 WHERE DATE_PART('month', release_date) = DATE_PART('month', CURRENT_DATE);