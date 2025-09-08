UPDATE uae_used_cars_staging
SET cylinders = CASE
    WHEN brand = 'audi' AND model = 'q5' THEN '4'
    WHEN brand = 'chevrolet' AND model = 'cruze' THEN '4'
    WHEN brand = 'chevrolet' AND model = 'suburban' THEN '8'
    WHEN brand = 'ford' AND model = 'f-series-pickup' THEN '6'
    WHEN brand = 'hyundai' AND model = 'h1' THEN '4'
    WHEN brand = 'hyundai' AND model = 'other' THEN NULL
    WHEN brand = 'isuzu' AND model = 'other' THEN NULL
    WHEN brand = 'lamborghini' AND model = 'urus' THEN '8'
    WHEN brand = 'land-rover' AND model = 'discovery-sport' THEN '4'
    WHEN brand = 'land-rover' AND model = 'range-rover-sport' THEN '6'
    WHEN brand = 'lincoln' AND model = 'nautilus' THEN '6'
    WHEN brand = 'mercedes-benz' AND model = 'glc' THEN '4'
    WHEN brand = 'mercedes-benz' AND model = 's-class-coupe' THEN '8'
    WHEN brand = 'mitsubishi' AND model = 'xpander' THEN '4'
    WHEN brand = 'nissan' AND model = 'altima' THEN '4'
    WHEN brand = 'nissan' AND model = 'sunny' THEN '4'
    WHEN brand = 'other-make' AND model = 'other-4x4' THEN NULL
    WHEN brand = 'porsche' AND model = 'carrera' THEN '6'
    WHEN brand = 'porsche' AND model = 'taycan' THEN 'EV'
    WHEN brand = 'renault' AND model = 'other' THEN NULL
    WHEN brand = 'suzuki' AND model = 'dzire' THEN '4'
    WHEN brand = 'tesla' AND model = 'model-3' THEN 'EV'
    WHEN brand = 'toyota' AND model = 'corolla' THEN '4'
    WHEN brand = 'toyota' AND model = 'hilux' THEN '4'
    WHEN brand = 'toyota' AND model = 'yaris' THEN '3'
    WHEN brand = 'volkswagen' AND model = 'id4' THEN 'EV'
    WHEN brand = 'volkswagen' AND model = 'other' THEN NULL
    ELSE cylinders
END

WHERE (brand, model) IN 
(
    ('audi', 'q5'),
    ('chevrolet', 'cruze'),
    ('chevrolet', 'suburban'),
    ('ford', 'f-series-pickup'),
    ('hyundai', 'h1'),
    ('hyundai', 'other'),
    ('isuzu', 'other'),
    ('lamborghini', 'urus'),
    ('land-rover', 'discovery-sport'),
    ('land-rover', 'range-rover-sport'),
    ('lincoln', 'nautilus'),
    ('mercedes-benz', 'glc'),
    ('mercedes-benz', 's-class-coupe'),
    ('mitsubishi', 'xpander'),
    ('nissan', 'altima'),
    ('nissan', 'sunny'),
    ('other-make', 'other-4x4'),
    ('porsche', 'carrera'),
    ('porsche', 'taycan'),
    ('renault', 'other'),
    ('suzuki', 'dzire'),
    ('tesla', 'model-3'),
    ('toyota', 'corolla'),
    ('toyota', 'hilux'),
    ('toyota', 'yaris'),
    ('volkswagen', 'id4'),
    ('volkswagen', 'other')
);
