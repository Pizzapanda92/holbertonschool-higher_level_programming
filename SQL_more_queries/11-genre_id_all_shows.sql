-- Lists all TV shows with their genre ID, including shows without a genre, sorted by show title and genre ID
SELECT tv_shows.title,
    tv_show_genres.genre_id
FROM tv_shows
    LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title ASC,
    tv_show_genres.genre_id ASC;