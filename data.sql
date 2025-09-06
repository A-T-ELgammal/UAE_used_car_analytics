SELECT brand, model , COUNT(cylinders) AS "unkown_cylinders_records"
FROM uae_used_cars_staging
WHERE cylinders  = 'Unknown'
GROUP BY brand, model;
