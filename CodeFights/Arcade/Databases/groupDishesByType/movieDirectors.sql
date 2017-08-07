/* Name: movieDirectors.sql
   Author: Robin Goyal
   Last-Modified: August 7, 2017
   Purpose: Return the directors who have shot movies after the year 2000
            and received more than 2 oscars for those movies
*/

CREATE PROCEDURE movieDirectors()
BEGIN
    SELECT director
    FROM (SELECT *
          FROM moviesInfo
          WHERE year > 2000) AS filter
    GROUP BY filter.director
    HAVING SUM(filter.oscars) > 2;
END