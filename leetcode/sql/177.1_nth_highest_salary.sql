#-------------------------------------------------------------------------------
#    Nth Highest Salary
#-------------------------------------------------------------------------------
# By Ying Peng
# https://leetcode.com/problems/nth-highest-salary/
# Completed 11/18/20
#-------------------------------------------------------------------------------

"""
1. ORDER DESC
2. Use Max to return null if result is empty
"""

CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
DECLARE M INT;
SET M = N - 1;
    RETURN (
        SELECT MAX(s.Salary)
        FROM(
            SELECT DISTINCT Salary
            FROM Employee
            ORDER BY Salary DESC
            LIMIT 1 OFFSET M
        ) s
    );
END