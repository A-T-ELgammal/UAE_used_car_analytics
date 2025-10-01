SELECT p_year, price
FROM uae_used_cars_cleaned
GROUP BY p_year, price
ORDER BY p_year DESC;