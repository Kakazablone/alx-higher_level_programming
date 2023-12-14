-- uses the hbtn_0d_tvshows database to lists all genres of the show Dexter
-- Results be sorted in ascending order by the genre name
SELECT tv_genres.name AS name
FROM tv_show_genres
INNER JOIN tv_genres
ON tv_show_genres.genre_id = tv_genres.id
INNER JOIN tv_shows
ON tv_show_genres.show_id = tv_shows.id
WHERE title = "Dexter"
ORDER BY name;
