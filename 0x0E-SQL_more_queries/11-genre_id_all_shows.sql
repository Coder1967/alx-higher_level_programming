-- script that lists all shows contained in the database hbtn_0d_tvshows.

SELECT tv.title, tg.genre_id
FROM tv_shows AS tv
LEFT JOIN tv_show_genres
AS tg ON tv.id = tg.show_id
ORDER  BY tv.title, tg.genre_id ASC;
