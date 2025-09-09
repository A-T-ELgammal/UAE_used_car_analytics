SELECT emirate , COUNT(emirate)
FROM uae_used_cars_staging
GROUP BY emirate;