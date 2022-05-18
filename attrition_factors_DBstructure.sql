--DROP TABLE personal_factors;

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

SELECT * FROM personal_factors;

--DROP TABLE work_factors;

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

SELECT * FROM work_factors;
