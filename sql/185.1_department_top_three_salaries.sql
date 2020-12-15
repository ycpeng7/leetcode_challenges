/*-------------------------------------------------------------------------------
#    Department Top Three Salaries
#-------------------------------------------------------------------------------
# By Ying Peng
# https://leetcode.com/problems/department-top-three-salaries/
# Completed 12/12/20
-------------------------------------------------------------------------------*/


SELECT Department, Employee, Salary
FROM(
    SELECT d.Name as Department, e.Name as Employee, Salary,
             DENSE_RANK() OVER(PARTITION BY d.Name ORDER BY Salary DESC) as salary_rank
    FROM Employee e INNER JOIN Department d
    ON e.DepartmentId = d.Id
) t
WHERE salary_rank <= 3
ORDER BY Department, Salary DESC