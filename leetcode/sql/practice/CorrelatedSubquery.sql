/*
Use the populated tables in the MySQL sandbox on Coderpad.io (https://coderpad.io/sandbox)
to answer the following question,
but without using any functions specific to MySQL (i.e. most be supported on all flavors of SQL) 

employees                             projects
+---------------+---------+           +---------------+---------+
| id            | int     |<----+  +->| id            | int     |
| first_name    | varchar |     |  |  | title         | varchar |
| last_name     | varchar |     |  |  | start_date    | date    |
| salary        | int     |     |  |  | end_date      | date    |
| department_id | int     |--+  |  |  | budget        | int     |
+---------------+---------+  |  |  |  +---------------+---------+
                             |  |  |
departments                  |  |  |  employees_projects
+---------------+---------+  |  |  |  +---------------+---------+
| id            | int     |<-+  |  +--| project_id    | int     |
| name          | varchar |     +-----| employee_id   | int     |
+---------------+---------+           +---------------+---------+


*/


-- Find the employees in each department with the 2 highest salaries for their department.

SELECT first_name, department_id, salary
FROM employees e1
WHERE salary >= (
    SELECT MAX(salary)
    FROM employees e2
    WHERE e2.department_id = e1.department_id
    AND salary < (SELECT MAX(salary) FROM employees)
);