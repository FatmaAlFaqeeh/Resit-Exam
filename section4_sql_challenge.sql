import mysql.connector

mydb = mysql.connector.connect(
    host= "127.0.0.1",
    user="root",
    password="",
    database="FatmaResitExam"
)

--4.1
UPDATE showings
SET available_seats = 0
WHERE movie_ID = 2
AND screen_ID = 9;



--4.2
SELECT *
FROM movie_info
WHERE age_rating IN ('PG', 'U');



--4.3
SELECT DISTINCT mi.movie_name
FROM movie_info mi
JOIN showings s ON mi.movie_ID = s.movie_ID
JOIN screens sc ON s.screen_ID = sc.screen_ID
WHERE sc.four_k = FALSE;



--4.4
SELECT mi.movie_name, s.start_time
FROM movie_info mi
JOIN showings s ON mi.movie_ID = s.movie_ID
JOIN (
    SELECT MAX(available_seats) AS max_seats
    FROM showings
) max_showings ON s.available_seats = max_showings.max_seats;




--4.5
SELECT
    mi.movie_name,
    s.start_time,
    ADDTIME(s.start_time, CAST(movie_length AS CHAR)) AS end_time
FROM
    movie_info mi
JOIN
    showings s ON mi.movie_ID = s.movie_ID;

