-- Write a script that lists all shows contained in hbtn_0d_tvshows without a genre linked
SELECT tv.title, tg.genre_id
FROM tv_shows AS tv LEFT JOIN tv_show_genres AS
tg ON tv.id = tg.show_id
where tg.genre_id IS NULL
ORDER  BY tv.title ASC;
