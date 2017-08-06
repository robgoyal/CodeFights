/* Name: newsSubscribers.sql
   Author: Robin Goyal
   Last-Modified: August 5, 2017
   Purpose: Return all the users subscribed to a newspaper with the word Daily in it from two tables
*/

CREATE PROCEDURE newsSubscribers()
BEGIN
    SELECT full_year.subscriber
    FROM full_year
    WHERE full_year.newspaper LIKE '%DAILY%'
    UNION
    SELECT half_year.subscriber
    FROM half_year
    WHERE half_year.newspaper LIKE '%DAILY%'
    ORDER BY subscriber;
END