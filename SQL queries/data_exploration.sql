
-- age count employees
SELECT COUNT(p."Age"), p."Age"
INTO age_count
FROM personal_factors AS p
GROUP BY "Age"
ORDER BY COUNT DESC;

SELECT * FROM age_count;


-- attrition age count
SELECT COUNT(p."Age"), p."Age"
INTO age_attrition
FROM personal_factors AS p
WHERE "Attrition" = 'Yes'
GROUP BY "Age"
ORDER BY COUNT DESC;

SELECT * FROM age_attrition;


-- working age count
SELECT COUNT(p."Age"), p."Age"
INTO age_working
FROM personal_factors AS p
WHERE "Attrition" = 'No'
GROUP BY "Age"
ORDER BY COUNT DESC;

SELECT * FROM age_working;


-- age comparison working v. quit
SELECT w."Age" as "Working Age",
	q."Age" as "Quit Age"
INTO age_comparison
FROM age_attrition AS q
FULL OUTER JOIN age_working AS w
ON (w.ID_age=q.ID_age);

-- add IDs to join
ALTER TABLE age_attrition ADD ID_age SERIAL;
ALTER TABLE age_working ADD ID_age SERIAL;
SELECT * FROM age_comparison;


-- monthly income
SELECT w."Employee Number", w."Monthly Income"
INTO emp_income
FROM work_factors AS w
ORDER BY "Monthly Income" DESC;

SELECT * FROM emp_income;


-- income quit
SELECT w."Monthly Income"
INTO income_quit
FROM work_factors AS w
WHERE "Attrition" = 'Yes'
ORDER BY "Monthly Income" DESC;

-- add ID to joing
ALTER TABLE income_quit ADD ID_income SERIAL;
SELECT * FROM income_quit;


-- income still working
SELECT w."Monthly Income"
INTO income_working
FROM work_factors AS w
WHERE "Attrition" = 'No'
ORDER BY "Monthly Income" DESC;

-- add ID to join
ALTER TABLE income_working ADD ID_income SERIAL;
SELECT * FROM income_working;


-- income comparison working v. quit
SELECT w."Monthly Income" as "Working Income",
	q."Monthly Income" as "Quit Income"
INTO income_comparison
FROM income_working AS w
FULL OUTER JOIN income_quit AS q
ON (w.ID_income=q.ID_income);

SELECT * FROM income_comparison;


-- distance from home quit
SELECT COUNT(p."Distance from Home"), p."Distance from Home"
INTO distance_quit
FROM personal_factors AS p
WHERE "Attrition" = 'Yes'
GROUP BY "Distance from Home"
ORDER BY COUNT DESC;

SELECT * FROM distance_quit;


-- distance from home still working
SELECT COUNT(p."Distance from Home"), p."Distance from Home"
INTO distance_working
FROM personal_factors AS p
WHERE "Attrition" = 'No'
GROUP BY "Distance from Home"
ORDER BY COUNT DESC;

SELECT * FROM distance_working;


-- distance from home comparison working v. quit
SELECT w."Distance from Home" as "Distance Working",
	q."Distance from Home" as "Distance Quit"
INTO distance_comparison
FROM distance_working AS w
FULL OUTER JOIN distance_quit AS q
ON (w.ID_distance=q.ID_distance);

-- add IDs to joing
ALTER TABLE distance_working ADD ID_distance SERIAL;
ALTER TABLE distance_quit ADD ID_distance SERIAL;
SELECT * FROM distance_comparison;

