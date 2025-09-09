SELECT emirate, COUNT(emirate) AS count
FROM uae_used_cars_staging 
GROUP BY emirate;

