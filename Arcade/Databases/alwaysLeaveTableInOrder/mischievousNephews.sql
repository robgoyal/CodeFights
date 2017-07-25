/* Name: michievousNephews.sql
   Author: Robin Goyal
   Last-Modified: July 25, 2017
   Purpose: Return all columns and the weekday of your mischievous nephews
            activites and order by weekday, author, mischief_date, and title
*/

CREATE PROCEDURE mischievousNephews()
BEGIN
    SELECT WEEKDAY(mischief_date) as weekday, mischief_date, author, title
    FROM mischief
    ORDER BY weekday,
        CASE author
            WHEN 'Huey' THEN 1
            WHEN 'Dewey' THEN 2
            WHEN 'Louie' THEN 3
        END, mischief_date, title;
END
