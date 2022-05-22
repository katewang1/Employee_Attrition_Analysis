-- personal factors table
CREATE TABLE personal_factors (
	"Age" INT,
	"Distance from Home" INT,
	"Education Level" INT,
	"Education Field" VARCHAR,
	"Employee Number" INT PRIMARY KEY,
	FOREIGN KEY ("Employee Number") REFERENCES work_factors ("Employee Number"),
	"Gender" VARCHAR (7),
	"Marital Status" VARCHAR,
	"Number Companies Worked" INT,
	"Over 18" VARCHAR (1),
	"Relationship Satisfaction" INT,
	"Total Working Years" INT,
	"Work Life Balance" INT,
	"Attrition" VARCHAR (3)
);


--professional factors table
CREATE TABLE work_factors (
	"Business Travel" VARCHAR (17),
	"Daily Rate" INT,
	"Department" VARCHAR (22),
	"Employee Count" INT,
	"Employee Number" INT PRIMARY KEY,
	"Environment Satisfaction" INT,
	"Hourly Rate" INT,
	"Job Involvement" INT,
	"Job Level" INT,
	"Job Role" VARCHAR,
	"Job Satisfaction" INT,
	"Monthly Income" INT,
	"Monthly Rate" INT,
	"Overtime" VARCHAR (3),
	"Percent Salary Hike" INT,
	"Performance Rating" INT,
	"Standard Hours" INT,
	"Stock Option Level" INT,
	"Training Times Last Year" INT,
	"Years at Company" INT,
	"Years In Current Role" INT,
	"Years Since Last Promotion" INT,
	"Years With Current Manager" INT,
	"Attrition" VARCHAR (3)
);


-- original dataset for storage and export
SELECT p."Age",
	p."Attrition",
	w."Business Travel",
	w."Daily Rate",
	w."Department",
	p."Distance from Home",
	p."Education Level",
	p."Education Field",
	w."Employee Count",
	w."Employee Number",
	w."Environment Satisfaction",
	p."Gender",
	w."Hourly Rate",
	w."Job Involvement",
	w."Job Level",
	w."Job Role",
	w."Job Satisfaction",
	p."Marital Status",
	w."Monthly Income",
	w."Monthly Rate",
	p."Number Companies Worked",
	p."Over 18",
	w."Overtime",
	w."Percent Salary Hike",
	w."Performance Rating",
	p."Relationship Satisfaction",
	w."Standard Hours",
	w."Stock Option Level",
	p."Total Working Years",
	w."Training Times Last Year",
	p."Work Life Balance",
	w."Years at Company",
	w."Years In Current Role",
	w."Years Since Last Promotion",
	w."Years With Current Manager"
INTO OG_dataset
FROM personal_factors AS p
INNER JOIN work_factors AS w
ON (p."Employee Number"=w."Employee Number");

