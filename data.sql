UPDATE uae_used_cars_staging
SET emirate = CASE
    WHEN emirate = ' Ajman' THEN 'Ajman'
    WHEN emirate = ' Dubai' THEN 'Dubai'
    WHEN emirate = ' Al Ain' THEN 'Al Ain'
    WHEN emirate = ' Ras Al Khaimah' THEN 'Ras Al Khaimah'
    WHEN emirate = ' Fujeirah' THEN 'Fujeirah'
    WHEN emirate = ' Umm Al Qawain' THEN 'Umm Al Qawain'
    WHEN emirate = ' Abu Dhabi' THEN ' Abu Dhabi'
    WHEN emirate = ' Sharjah' THEN 'Sharjah'
    ELSE emirate
END
WHERE emirate IN (' Ajman', ' Dubai', ' Al Ain', ' Ras Al Khaimah', ' Umm Al Qawain', ' Abu Dhabi', ' Sharjah')


SELECT emirate, COUNT(emirate) AS count
FROM uae_used_cars_staging 
GROUP BY emirate;