-- record should display: <TV Show genre> - <Number of shows linked to this genre>
SELECT tv_genres. name AS 'genre', COUNT(tv_show_genres.genre_id) AS 'number_of_shows' FROM tv_genres LEFT JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id WHERE tv_show_genres.genre_id IS NOT NULL GROUP BY tv_genres.name;
