-- If a show doesn’t have a genre, display NULL in the genre column
-- tv_shows || tv_genres || tv_show_genres
SELECT tv_shows.title AS title, tv_genres.name AS tv_genres FROM tv_shows LEFT JOIN tv_show_genres ON tv_show_genres.show_id = tv_shows.id LEFT JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id ORDER BY tv_shows.title ASC, tv_genres.name ASC; 
