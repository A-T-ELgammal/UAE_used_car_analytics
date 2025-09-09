UPDATE uae_used_cars_staging
SET transmission_type = CASE
    WHEN transmission_type = 'Automatic Transmission' THEN 'Automatic'
    WHEN transmission_type = 'Manual Transmission' THEN 'Manual'
END

    WHERE transmission_type IN ('Automatic Transmission', 'Manual Transmission')