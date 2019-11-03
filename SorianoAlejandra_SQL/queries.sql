SELECT  emp.emp_no,
       emp.last_name,
       emp.first_name,
       emp.gender
FROM employees as emp
ORDER BY emp.emp_no;

SELECT  dm.dept_no,
       d.dept_name,
       dm.emp_no,
       e.last_name,
       e.first_name,
       dm.from_date,
       dm.to_date
FROM dept_manager AS dm
   INNER JOIN departments AS d
       ON (dm.dept_no = d.dept_no)
   INNER JOIN employees AS e
       ON (dm.emp_no = e.emp_no);


SELECT 
	e.emp_no,
	dm.dept_no
FROM employees AS e
	INNER JOIN dept_manager AS dm
		ON (e.emp_no=dm.emp_no);

SELECT  e.emp_no,
       e.last_name,
       e.first_name,
       d.dept_name
FROM employees AS e
   INNER JOIN deptemployees AS de
       ON (e.emp_no = de.emp_no)
   INNER JOIN departments AS d
       ON (de.dept_no = d.dept_no)
WHERE d.dept_name = 'Sales'
ORDER BY e.emp_no;


SELECT last_name, COUNT(last_name)
FROM employees
GROUP BY last_name
ORDER BY COUNT(last_name) DESC;