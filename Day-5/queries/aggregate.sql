-- 1. Total number of employees in each department
SELECT department, COUNT(*) AS total_employees
FROM employees
GROUP BY department;

-- 2. Average salary per department
SELECT department, AVG(salary) AS avg_salary
FROM employees
GROUP BY department;

-- 3. Maximum salary in company
SELECT MAX(salary) FROM employees;

-- 4. Total salary per department
SELECT department, SUM(salary)
FROM employees GROUP BY department;

-- 5. Departments with more than 2 employees
SELECT department, COUNT(*)
FROM employees
GROUP BY department
HAVING COUNT(*) > 2;

-- 6. Min & Max order amount
SELECT MIN(amount), MAX(amount)
FROM orders;

-- 7. Total spent by each customer
SELECT customer_id, SUM(amount)
FROM orders GROUP BY customer_id;

-- 8. Customers spending > 500
SELECT customer_id, SUM(amount)
FROM orders
GROUP BY customer_id
HAVING SUM(amount) > 500;

-- 9. Revenue per region
SELECT region, SUM(revenue)
FROM sales GROUP BY region;

-- 10. Avg revenue per salesperson > 400
SELECT salesperson, AVG(revenue)
FROM sales
GROUP BY salesperson
HAVING AVG(revenue) > 400;
