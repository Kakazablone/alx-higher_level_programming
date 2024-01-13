-- Displays the rows in descending order by score and name
SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
