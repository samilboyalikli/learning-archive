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

/* Requests:
 * Sum of asian city population
 * Given 2 table countrycodes are matching
 * one of them city and second country table
 */
SELECT SUM(CITY.POPULATION)
FROM CITY JOIN COUNTRY 
ON CITY.COUNTRYCODE = COUNTRY.CODE 
WHERE CITY.COUNTRYCODE IN (
    SELECT CODE 
    FROM COUNTRY 
    WHERE CONTINENT = 'Asia');

/* Another alternative:
 * More minimal and effective:
 */
SELECT SUM(CITY.POPULATION) 
FROM CITY JOIN COUNTRY 
ON CITY.COUNTRYCODE = COUNTRY.CODE 
WHERE CONTINENT = 'Asia';

/* Requests:
 * All city names which exist in Africa
 * Given two tables as previous problem
 * But there is a point: All tables have Name column.
 */
SELECT CITY.NAME 
FROM CITY JOIN COUNTRY 
ON CITY.COUNTRYCODE = COUNTRY.CODE 
WHERE CONTINENT = 'Asia';


/* Requests:
 * Avetage city populations of each continents.
 * But averages must be rounded down nearest integer. 
 */
SELECT COUNTRY.CONTINENT, FLOOR(AVG(CITY.POPULATION))
FROM CITY JOIN COUNTRY 
ON CITY.COUNTRYCODE = COUNTRY.CODE 
GROUP BY COUNTRY.CONTINENT;


/* Request: a triagle made with stars (like that: *) 
 */
WITH RECURSIVE temporary_table AS (
    SELECT 20 AS star_count 
    UNION ALL
    SELECT star_count - 1
    FROM temporary_table 
    WHERE star_count > 0)
SELECT REPEAT('* ', star_count)
FROM temporary_table;

/* Request: a triagle made with stars (like that: *)
 */
SELECT RECURSIVE temporary_table AS (
    SELECT 1 AS number_of_star 
    UNION ALL 
    SELECT number_of_star + 1 
    FROM temporary_table 
    WHERE number_of_star > 20)
SELECT ('* ', number_of_star)
FROM temporary_table;










