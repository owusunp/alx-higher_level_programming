-- a script that uses the hbtn_0d_tvshows database to lists all genres of the show Dexter. table 1  tv_genres table 2 tv_show_genres t3 tv_shows
SELECT tv_genres.name AS name FROM ((tv_genres LEFT JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id) LEFT JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id) WHERE tv_show_genres.show_id = 8 ORDER BY tv_genres.name ASC;
