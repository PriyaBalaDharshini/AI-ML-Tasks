-- Task 1: Basic Querying

select * FROM  employees WHERE department='Marketing';

SELECT name, department, salary from  employees where salary >=90000

SELECT * FROM  employees WHERE department='Sales' or department='Finance'

-- Task 2: Sorting and Limiting

select name, salary from employees ORDER BY salary DESC limit 5;

select name, hire_date, department from employees where department='Engineering' ORDER BY hire_date DESC limit 5

select name, hire_date, salary, department from employees where salary >= 70000 and department!= HR ORDER BY hire_date asc limit 1


-- Task 3: Calculated Fields and Aliases

select name, salary , salary/12 as monthly_salary from employees where salary>=60000

select name as employee_name, salary as annual_salary, salary/12 as monthly_salary
from employees
where department='Finance'
order by salary DESC
