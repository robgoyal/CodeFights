/* Name: monthlyScholarships.sql
   Author: Robin Goyal
   Last-Modified: July 23, 2017
   Purpose: Return the table with scholarships display the monthly payout
*/
    
CREATE PROCEDURE monthlyScholarships()
BEGIN
    SELECT i, scholarship / 12 as scholarship FROM scholarships;
END