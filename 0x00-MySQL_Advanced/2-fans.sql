-- Write a SQL script that ranks country origins of bands, ordered by the number of (non-unique) fans
-- Column names must be: origin and nb_fans
SELECT origin, fans FROM metal_bands ORDER BY fans DESC;
