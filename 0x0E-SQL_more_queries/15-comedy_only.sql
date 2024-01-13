-- Lists all Comedy shows
SELECT tv_shows.title AS title
FROM tv_show_genres
INNER JOIN  tv_shows
ON tv_show_genres.show_id = tv_shows.id
INNER JOIN tv_genres
ON tv_show_genres.genre_id = tv_genres.id
WHERE name = "Comedy"
ORDER BY title;
