INSERT INTO uae_used_cars_cleaned 
SELECT 
    brand,
    model,
    p_year::INT,
    price::INT,
    milage::INT,
    body_type::VARCHAR(25),
    cylinders::INT,
    transmission_type::VARCHAR(10),
    fuel_type::VARCHAR(10),
    color,
    emirate,
    description
FROM uae_used_cars_staging

