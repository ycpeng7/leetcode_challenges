#-------------------------------------------------------------------------------
#    Second Highest Salary
#-------------------------------------------------------------------------------
# By Ying Peng
# https://leetcode.com/problems/second-highest-salary/
# Completed 11/18/20
#-------------------------------------------------------------------------------

"""
1. Use window function DENSE_RANK
2. Use max to return NULL if value doesn't exist
"""


SELECT MAX(t.Salary) AS SecondHighestSalary
FROM (SELECT DISTINCT Salary, DENSE_RANK() OVER(ORDER BY Salary DESC) as salary_rank
      FROM Employee) t
WHERE t.salary_rank = 2