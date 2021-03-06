-- Write a SQL script that lists all bands with Glam rock as their main style, ranked by their longevity
--    Column names must be: band_name and lifespan (in years) - You should use attributes formed and split for computing the lifespan
Select band_name, SUM(split  - formed) lifespan
FROM metal_bands
WHERE LOCATE('Glam rock', style)
GROUP BY band_name;
