/* Name: itemCounts.sql
   Author: Robin Goyal
   Last-Modified: August 7, 2017
   Purpose: Return a table which contains the names of items, their types and
            the amount of those items
*/

CREATE PROCEDURE itemCounts()
BEGIN
    SELECT item_name, item_type, COUNT(item_name) as item_count
    FROM availableItems
    GROUP BY item_name, item_type
    ORDER BY item_type, item_name;
END