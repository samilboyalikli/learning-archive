/* There is two required:
 * Sum of all values in LAT_N rounded to a scale of 2 decimal.
 * Sum of all values in LONG_W rounded to a scale of 2 decimal. 
 */
SELECT ROUND(SUM(LAT_N),2), ROUND(SUM(LONG_W),2) 
FROM STATION;

/* There is two required:
 * Sum of LAT_N having values greater than 38.7880 and less than 137.2345.
 * Answer should be rounded 2 decimal.
 */
SELECT ROUND(SUM(LAT_N),4) 
FROM STATION
WHERE LAT_N > 38.7880
  AND LAT_N < 137.2345;

