/*-------------------------------------------------------------------------------
#    Exchange Seats
#-------------------------------------------------------------------------------
# By Ying Peng
# https://leetcode.com/problems/department-top-three-salaries/
# Completed 12/13/20
-------------------------------------------------------------------------------*/

SELECT id,
CASE
    WHEN id = (SELECT MAX(id) FROM seat) AND mod(id,2) = 1 THEN student
    WHEN mod(id,2) = 0 THEN LAG(student) OVER(ORDER BY id)
    WHEN mod(id,2) = 1 THEN LEAD(student) OVER(ORDER BY id)
END as student
FROM seat;