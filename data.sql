SELECT brand , COUNT(brand)
        
FROM uae_used_cars_staging
GROUP BY brand;

SELECT model , COUNT(model)
        
FROM uae_used_cars_staging
GROUP BY model;

SELECT body_type , COUNT(body_type)
        
FROM uae_used_cars_staging
GROUP BY body_type;

SELECT fuel_type , COUNT(fuel_type)
        
FROM uae_used_cars_staging
GROUP BY fuel_type;

SELECT color , COUNT(color)
        
FROM uae_used_cars_staging
GROUP BY color;
