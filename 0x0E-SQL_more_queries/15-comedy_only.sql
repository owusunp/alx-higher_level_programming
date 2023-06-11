-- tv_genres table contains only one record where name = Comedy (but the id can be different)
-- tablee 1 tv_shows table 2 tv_genres table 3 tv_show_genres
SELECT tv_shows.title FROM ((tv_shows INNER JOIN tv_show_genres ON tv_show_genres.show_id = tv_shows.id) INNER JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id) WHERE tv_genres.name = 'Comedy' ORDER BY tv_shows.title ASC;
