-- select p_year, price, milage, cylinders
-- FROm uae_used_cars_staging
-- WHERE p_year = '[A-Za-z]' OR
--         price = '[A-Za-z]' OR 
--         milage = '[A-Za-z]' OR
--         cylinders = '[A-Za-z]'
--         OR ;

SELECT *
FROM uae_used_cars_staging
WHERE p_year = '[A-Za-z]' 
    OR price = '[A-Za-z]'
    OR milage = '[A-Za-z]'
    OR cylinders = '[A-Za-z]'
    OR p_year IS NULL
    OR price IS NULL
    OR milage IS NULL
    OR cylinders IS NULL;