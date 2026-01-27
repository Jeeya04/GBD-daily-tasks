-- ==============================
-- TASK 2 : PART 2
-- ==============================

-- 1. Employee list in ascending order of salary
SELECT * FROM Employee
ORDER BY Salary ASC;

-- 2. Distinct salary from Employee table
SELECT DISTINCT Salary FROM Employee;

-- 3. Total number of active employees
SELECT COUNT(*) AS ActiveEmployees
FROM Employee
WHERE Active = 1;

-- 4. Update the Department of Nancy to HR
UPDATE Employee
SET DepartmentId = 3
WHERE Name = 'Nancy';

-- 5. Employee with highest and second highest salary
SELECT *
FROM Employee
WHERE Salary IN (
    SELECT MAX(Salary) FROM Employee
    UNION
    SELECT MAX(Salary) FROM Employee
    WHERE Salary < (SELECT MAX(Salary) FROM Employee)
);

-- 6. Department name of each employee
SELECT e.Name, d.Name AS Department
FROM Employee e
JOIN Department d ON e.DepartmentId = d.Id;

-- 7. Department name with maximum employee count
SELECT d.Name, COUNT(e.Id) AS EmpCount
FROM Employee e
JOIN Department d ON e.DepartmentId = d.Id
GROUP BY d.Name
ORDER BY EmpCount DESC
LIMIT 1;

-- 8. Departments where no Employee is assigned
SELECT d.Name
FROM Department d
LEFT JOIN Employee e ON d.Id = e.DepartmentId
WHERE e.Id IS NULL;

-- 9. Employee list with same salary
SELECT Salary, GROUP_CONCAT(Name) AS Employees
FROM Employee
GROUP BY Salary
HAVING COUNT(*) > 1;
