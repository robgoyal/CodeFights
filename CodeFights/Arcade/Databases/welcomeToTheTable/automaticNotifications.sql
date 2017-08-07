/* Name: automaticNotifications.sql
   Author: Robin Goyal
   Last-Modified: July 23, 2017
   Purpose: Return the email of users who aren't admin or premium
*/

CREATE PROCEDURE automaticNotifications()
    SELECT email
    FROM users
    WHERE role NOT IN ("admin", "premium")
    ORDER BY email;
