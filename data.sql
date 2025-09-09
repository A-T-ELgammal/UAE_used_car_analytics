UPDATE uae_used_cars_staging
SET cylinders = '0'
WHERE cylinders ='None' OR cylinders = 'EV';

SELECT DISTINCT cylinders
FROM uae_used_cars_staging