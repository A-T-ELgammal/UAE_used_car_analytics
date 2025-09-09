UPDATE uae_used_cars_staging
SET emirate = CASE
    WHEN emirate = ' Abu Dhabi' THEN 'Abu Dhabi'
    WHEN emirate = ' Fujeirah' THEN ' Fujeirah'
ELSE emirate
END

WHERE emirate IN (' Abu Dhabi', ' Fujeirah')