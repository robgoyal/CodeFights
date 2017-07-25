/* Name: testCheck.sql
   Author: Robin Goyal
   Last-Modified: July 25, 2017
   Purpose: Check whether a students answers are correct, incorrect or no
            answer from given_answer and correct_answer
*/

CREATE PROCEDURE testCheck()
    SELECT id, IF(given_answer IS NULL, 'no answer',
                  IF(correct_answer = given_answer, 'correct', 'incorrect')) AS checks
    FROM answers
    ORDER BY id