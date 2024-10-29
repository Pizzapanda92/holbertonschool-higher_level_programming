-- list all records with a score >= 10 of table in order of score and whit name
SELECT score,
    name
FROM second_table
WHERE score >= 10
ORDER BY score DESC;