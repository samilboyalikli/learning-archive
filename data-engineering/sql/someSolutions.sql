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

/* Requests:
 * Maximum LAT_N value between all LAT_N values which rounded 4 decimal.
 * LAT_N values should be less than 137.2345.
 */
SELECT MAX(ROUND(LAT_N,4)) 
FROM STATION 
WHERE LAT_N < 137.2345;

/* Requests:
 * Western longitude rounded 4 decimal
 * which largest nothern logitude less than 137.2345
 */
SELECT ROUND(LONG_W,4) 
FROM STATION 
WHERE LAT_N = (
    SELECT MAX(LAT_N) 
    FROM STATION 
    WHERE LAT_N < 137.2345);

/* Requests:
 * Southernmost norht latitude rounded 4 decimal
 * which biggest than 38.7780.
 */
SELECT ROUND(MIN(LAT_N),4) 
FROM STATION 
WHERE LAT_N > 38.7780;

/* Requests:
 * Western longitude rounded 4 decimal
 * which southernmost north latitude biggest than 38.7780.
 */
SELECT ROUND(LONG_W,4) 
FROM STATION 
WHERE LAT_N = (
    SELECT MIN(LAT_N) 
    FROM STATION 
    WHERE LAT_N > 38.7780);







