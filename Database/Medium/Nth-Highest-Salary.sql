/*
Table: Employee

+-------------+------+
| Column Name | Type |
+-------------+------+
| id          | int  |
| salary      | int  |
+-------------+------+
id is the primary key (column with unique values) for this table.
Each row of this table contains information about the salary of an employee.
 

Write a solution to find the nth highest distinct salary from the Employee table. If there are less than n distinct salaries, return null.

The result format is in the following example.

 

Example 1:

Input: 
Employee table:
+----+--------+
| id | salary |
+----+--------+
| 1  | 100    |
| 2  | 200    |
| 3  | 300    |
+----+--------+
n = 2
Output: 
+------------------------+
| getNthHighestSalary(2) |
+------------------------+
| 200                    |
+------------------------+
Example 2:

Input: 
Employee table:
+----+--------+
| id | salary |
+----+--------+
| 1  | 100    |
+----+--------+
n = 2
Output: 
+------------------------+
| getNthHighestSalary(2) |
+------------------------+
| null                   |
+------------------------+
*/

-- Neu tra ve Table thi phai Return Query (); de tra ve bang, con neu Returns INT thi khong can


-- FUNCTION TRA VE BANG
-- SELECT * FROM NthHighestSalary(2)
CREATE OR REPLACE FUNCTION NthHighestSalary(N INT) RETURNS TABLE (Salary INT) AS $$
BEGIN
    IF N <= 0 THEN
        RETURN;
    END IF;
    RETURN QUERY (
    -- Write your PostgreSQL query statement below.
    SELECT DISTINCT Employee.salary 
    FROM Employee 
    ORDER BY Employee.salary DESC
    LIMIT 1 OFFSET N-1
      
  );
END;
$$ LANGUAGE plpgsql;

-- FUNCTION TRA VE KIEU INTEGER
CREATE OR REPLACE FUNCTION NthHighestSalary(N INT)
RETURNS INT
LANGUAGE plpgsql
AS $$
DECLARE nth_salary INT;
BEGIN 
    SELECT DISTINCT E.salary into nth_salary
    FROM Employee as E
    ORDER BY E.salary DESC 
    OFFSET N-1
    LIMIT 1;
    RETURN nth_salary;
END;
$$;

-- SELECT NthHighestSalary(2)



