-- Databricks notebook source
CREATE OR REPLACE VIEW
  artists_by_year
AS SELECT
  artist_name,
  year
FROM
  song_data
WHERE
  year > 0;

SELECT
  artist_name,
  count(artist_name)
AS
  num_songs,
  year
FROM
  artists_by_year
GROUP BY
  artist_name,
  year
ORDER BY
  num_songs DESC,
  year DESC

-- COMMAND ----------

-- Find songs for your DJ list
 CREATE OR REPLACE VIEW
   danceable_songs
 AS SELECT
   artist_name,
   title,
   tempo
 FROM
   song_data
 WHERE
   time_signature = 4
   AND
   tempo between 100 and 140;

 SELECT * FROM danceable_songs limit 100

-- COMMAND ----------


