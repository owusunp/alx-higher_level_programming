-- tv_shows table contains only one record where title = Dexter (but the id can be different
-- table 1 tv_genres||tv_show_genres||tv_shows

SELECT DISTINCT tv_genres.name AS name FROM tv_genres INNER JOIN tv_show_genres ON tv_show_genres.genre_id = tv_genres.id INNER JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id WHERE tv_shows.id != 8 ORDER BY tv_genres.name; 
