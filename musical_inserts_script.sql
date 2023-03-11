INSERT INTO executors (nickname)
VALUES ('Би-2');

INSERT INTO executors (nickname)
VALUES ('Ленинград');

INSERT INTO executors (nickname)
VALUES ('Руки вверх');

INSERT INTO executors (nickname)
VALUES ('Баста');

INSERT INTO executors (nickname)
VALUES ('Макс Корж');

INSERT INTO executors (nickname)
VALUES ('Король и Шут');

INSERT INTO executors (nickname)
VALUES ('Maroon 5');

INSERT INTO executors (nickname)
VALUES ('Linkin Park');

INSERT INTO executors (nickname)
VALUES ('КИНО');

INSERT INTO executors (nickname)
VALUES ('Земфира');

INSERT INTO executors (nickname)
VALUES ('The Prodigy');

INSERT INTO genres (genre_name)
VALUES ('Русский рок');

INSERT INTO genres (genre_name)
VALUES ('Зарубежный рок');

INSERT INTO genres (genre_name)
VALUES ('Техно');

INSERT INTO genres (genre_name)
VALUES ('Зарубежная музыка');

INSERT INTO genres (genre_name)
VALUES ('Русская поп-музыка');

INSERT INTO genres (genre_name)
VALUES ('Рок');

INSERT INTO genres (genre_name)
VALUES ('Реп');

INSERT INTO albums (album_name, release_date)
VALUES ('Горизон событий', '2017-09-29');

INSERT INTO albums (album_name, release_date)
VALUES ('Би-2', '2000-05-20');

INSERT INTO albums (album_name, release_date)
VALUES ('Аврора', '2007-10-20');

INSERT INTO albums (album_name, release_date)
VALUES ('Баста 1', '2005-09-05');

INSERT INTO albums (album_name, release_date)
VALUES ('Сделай погромче', '2001-05-05');

INSERT INTO albums (album_name, release_date)
VALUES ('Жить в кайф', '2018-06-20');

INSERT INTO albums (album_name, release_date)
VALUES ('Камнем по голове', '1996-11-15');

INSERT INTO albums (album_name, release_date)
VALUES ('Red Pill Blues', '2017-08-23');

INSERT INTO albums (album_name, release_date)
VALUES ('Легенда', '1989-01-07');

INSERT INTO albums (album_name, release_date)
VALUES ('Meteora', '2003-12-18');

INSERT INTO albums (album_name, release_date)
VALUES ('До свидания...', '2000-04-27');

INSERT INTO albums (album_name, release_date)
VALUES ('Invaders Must Die', '2009-11-10');

INSERT INTO tracks (track_name, duration, album_id)
VALUES ('Группа крови', 239, 9);

INSERT INTO tracks (track_name, duration, album_id)
VALUES ('Перемен', 295, 9);

INSERT INTO tracks (track_name, duration, album_id)
VALUES ('Пачка сигарет', 268, 9);

INSERT INTO tracks (track_name, duration, album_id)
VALUES ('My bad', 333, 12);

INSERT INTO tracks (track_name, duration, album_id)
VALUES ('Дом мой', 333, 1);

INSERT INTO tracks (track_name, duration, album_id)
VALUES ('Вояж', 218, 3);

INSERT INTO tracks (track_name, duration, album_id)
VALUES ('ЗОЖ', 142, 3);

INSERT INTO tracks (track_name, duration, album_id)
VALUES ('Моя игра', 358, 4);

INSERT INTO tracks (track_name, duration, album_id)
VALUES ('Сансара', 325, 4);

INSERT INTO tracks (track_name, duration, album_id)
VALUES ('Жить в кайф', 263, 6);

INSERT INTO tracks (track_name, duration, album_id)
VALUES ('Малый повзрослел', 300, 6);

INSERT INTO tracks (track_name, duration, album_id)
VALUES ('П.М.М.Л', 217, 11);

INSERT INTO tracks (track_name, duration, album_id)
VALUES ('Крошка моя', 250, 5);

INSERT INTO tracks (track_name, duration, album_id)
VALUES ('Черное солнце', 289, 1);

INSERT INTO tracks (track_name, duration, album_id)
VALUES ('Лётчик', 351, 1);

INSERT INTO tracks (track_name, duration, album_id)
VALUES ('Варвара', 301, 2);

INSERT INTO tracks (track_name, duration, album_id)
VALUES ('Мой друг', 289, 2);

INSERT INTO tracks (track_name, duration, album_id)
VALUES ('Счастье', 246, 2);

INSERT INTO tracks (track_name, duration, album_id)
VALUES ('Эй, ухнем!', 165, 3);

INSERT INTO tracks (track_name, duration, album_id)
VALUES ('Дурак и молния', 114, 7);

INSERT INTO tracks (track_name, duration, album_id)
VALUES ('Мария', 263, 7);

INSERT INTO tracks (track_name, duration, album_id)
VALUES ('Lips On You', 216, 8);

INSERT INTO tracks (track_name, duration, album_id)
VALUES ('Faint', 164, 10);

INSERT INTO tracks (track_name, duration, album_id)
VALUES ('Numb', 187, 10);

INSERT INTO tracks (track_name, duration, album_id)
VALUES ('Omen', 216, 12);

INSERT INTO tracks (track_name, duration, album_id)
VALUES ('Мой рок-н-ролл', 405, 2);

INSERT INTO collections (collection_name, release_date)
VALUES ('Иди и смотри', '2010-11-26');

INSERT INTO collections (collection_name, release_date)
VALUES ('Были времена', '2022-02-03');

INSERT INTO collections (collection_name, release_date)
VALUES ('Танцуй', '2017-06-20');

INSERT INTO collections (collection_name, release_date)
VALUES ('Хиты 2016 ', '2016-12-15');

INSERT INTO collections (collection_name, release_date)
VALUES ('Новогоднее ', '2021-12-01');

INSERT INTO collections (collection_name, release_date)
VALUES ('Форсаж 9 ', '2021-05-13');

INSERT INTO collections (collection_name, release_date)
VALUES ('Summer Festival ', '2021-07-15');

INSERT INTO collections (collection_name, release_date)
VALUES ('Радио ', '2015-09-14');

INSERT INTO collections (collection_name, release_date)
VALUES ('Это качает! ', '2017-10-08');

INSERT INTO collections (collection_name, release_date)
VALUES ('Пробежка', '2015-06-01');

INSERT INTO collections (collection_name, release_date)
VALUES ('Хиты 2019', '2019-06-01');

INSERT INTO executors_genres (executor_id, genre_id)
VALUES (1, 1);

INSERT INTO executors_genres (executor_id, genre_id)
VALUES (1, 8);

INSERT INTO executors_genres (executor_id, genre_id)
VALUES (2, 1);

INSERT INTO executors_genres (executor_id, genre_id)
VALUES (2, 8);

INSERT INTO executors_genres (executor_id, genre_id)
VALUES (3, 7);

INSERT INTO executors_genres (executor_id, genre_id)
VALUES (4, 9);

INSERT INTO executors_genres (executor_id, genre_id)
VALUES (5, 7);

INSERT INTO executors_genres (executor_id, genre_id)
VALUES (5, 9);

INSERT INTO executors_genres (executor_id, genre_id)
VALUES (6, 1);

INSERT INTO executors_genres (executor_id, genre_id)
VALUES (6, 8);

INSERT INTO executors_genres (executor_id, genre_id)
VALUES (7, 6);

INSERT INTO executors_genres (executor_id, genre_id)
VALUES (8, 4);

INSERT INTO executors_genres (executor_id, genre_id)
VALUES (8, 6);

INSERT INTO executors_genres (executor_id, genre_id)
VALUES (8, 8);

INSERT INTO executors_genres (executor_id, genre_id)
VALUES (9, 1);

INSERT INTO executors_genres (executor_id, genre_id)
VALUES (9, 8);

INSERT INTO executors_genres (executor_id, genre_id)
VALUES (10, 1);

INSERT INTO executors_genres (executor_id, genre_id)
VALUES (10, 8);

INSERT INTO executors_genres (executor_id, genre_id)
VALUES (11, 5);

INSERT INTO executors_genres (executor_id, genre_id)
VALUES (11, 6);

INSERT INTO executors_albums (album_id, executor_id)
VALUES (1, 1);

INSERT INTO executors_albums (album_id, executor_id)
VALUES (2, 1);

INSERT INTO executors_albums (album_id, executor_id)
VALUES (3, 2);

INSERT INTO executors_albums (album_id, executor_id)
VALUES (4, 4);

INSERT INTO executors_albums (album_id, executor_id)
VALUES (5, 3);

INSERT INTO executors_albums (album_id, executor_id)
VALUES (6, 5);

INSERT INTO executors_albums (album_id, executor_id)
VALUES (7, 6);

INSERT INTO executors_albums (album_id, executor_id)
VALUES (8, 7);

INSERT INTO executors_albums (album_id, executor_id)
VALUES (9, 9);

INSERT INTO executors_albums (album_id, executor_id)
VALUES (10, 8);

INSERT INTO executors_albums (album_id, executor_id)
VALUES (11, 10);

INSERT INTO executors_albums (album_id, executor_id)
VALUES (12, 11);

INSERT INTO executors_albums (album_id, executor_id)
VALUES (1, 10);

INSERT INTO executors_albums (album_id, executor_id)
VALUES (4, 1);

INSERT INTO executors_albums (album_id, executor_id)
VALUES (4, 3);

INSERT INTO collections_tracks (collection_id , track_id)
VALUES (1, 10);

INSERT INTO collections_tracks (collection_id , track_id)
VALUES (1, 14);

INSERT INTO collections_tracks (collection_id , track_id)
VALUES (2, 1);

INSERT INTO collections_tracks (collection_id , track_id)
VALUES (2, 2);

INSERT INTO collections_tracks (collection_id , track_id)
VALUES (2, 3);

INSERT INTO collections_tracks (collection_id , track_id)
VALUES (3, 4);

INSERT INTO collections_tracks (collection_id , track_id)
VALUES (3, 11);

INSERT INTO collections_tracks (collection_id , track_id)
VALUES (4, 8);

INSERT INTO collections_tracks (collection_id , track_id)
VALUES (5, 11);

INSERT INTO collections_tracks (collection_id , track_id)
VALUES (5, 5);

INSERT INTO collections_tracks (collection_id , track_id)
VALUES (6, 20);

INSERT INTO collections_tracks (collection_id , track_id)
VALUES (7, 20);

INSERT INTO collections_tracks (collection_id , track_id)
VALUES (8, 4);

INSERT INTO collections_tracks (collection_id , track_id)
VALUES (8, 7);

INSERT INTO collections_tracks (collection_id , track_id)
VALUES (8, 8);

INSERT INTO collections_tracks (collection_id , track_id)
VALUES (8, 9);

INSERT INTO collections_tracks (collection_id , track_id)
VALUES (8, 22);

INSERT INTO collections_tracks (collection_id , track_id)
VALUES (9, 4);

INSERT INTO collections_tracks (collection_id , track_id)
VALUES (9, 21);

INSERT INTO collections_tracks (collection_id , track_id)
VALUES (9, 22);

INSERT INTO collections_tracks (collection_id , track_id)
VALUES (10, 8);

INSERT INTO collections_tracks (collection_id , track_id)
VALUES (10, 9);

INSERT INTO collections_tracks (collection_id , track_id)
VALUES (10, 20);

INSERT INTO collections_tracks (collection_id , track_id)
VALUES (10, 21);

INSERT INTO collections_tracks (collection_id , track_id)
VALUES (10, 22);

INSERT INTO collections_tracks (collection_id , track_id)
VALUES (10, 23);

INSERT INTO collections_tracks (collection_id , track_id)
VALUES (11, 2);

INSERT INTO collections_tracks (collection_id , track_id)
VALUES (11, 10);