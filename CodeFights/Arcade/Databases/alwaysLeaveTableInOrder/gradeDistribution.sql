/* Name: gradeDistribution.sql
   Author: Robin Goyal
   Last-Modified: July 25, 2017
   Purpose: Return the name and id of the students whose best grade comes
            from Option 3. Order by first 3 characters of student name and then
            by the ID
   Note: This solution became way too complex once I realized from other solutions
         that I was interpreting the question quite wrong
*/

CREATE PROCEDURE gradeDistribution()
BEGIN
    SELECT Name, Grades.ID
    FROM Grades
    INNER JOIN
    (
     SELECT Grades.ID, (0.25 * Midterm1 + 0.25 * Midterm2 + 0.5 * Final) AS Option1,
     (0.5 * Midterm1 + 0.5 * Midterm2) AS Option2, Final AS Option3
     FROM Grades
    ) T2
    ON T2.ID = Grades.ID
    WHERE GREATEST(T2.Option1, T2.Option2, T2.Option3) = Grades.Final AND T2.Option3 != T2.Option1 AND T2.Option3 != T2.Option2
    ORDER BY LEFT(Name, 3) ASC, ID;
END