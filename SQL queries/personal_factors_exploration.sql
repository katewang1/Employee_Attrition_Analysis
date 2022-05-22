SELECT * FROM personal_factors;

DROP TABLE age_count;
-- age count employees
SELECT COUNT(p."Age"), p."Age"
INTO age_count
FROM personal_factors AS p
GROUP BY "Age"
ORDER BY COUNT DESC;

SELECT * FROM age_count;

DROP TABLE age_attrition;
-- attrition age count
SELECT COUNT(p."Age"), p."Age"
INTO age_attrition
FROM personal_factors AS p
WHERE "Attrition" = 'Yes'
GROUP BY "Age"
ORDER BY COUNT DESC;

SELECT * FROM age_attrition;


SELECT * FROM work_factors;

DROP TABLE emp_income;
-- monthly income
SELECT w."Monthly Income"
INTO emp_income
FROM work_factors AS w
ORDER BY "Monthly Income" DESC;

SELECT * FROM emp_income;


