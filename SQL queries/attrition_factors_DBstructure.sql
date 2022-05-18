DROP TABLE personal_factors;
-- personal factors table
CREATE TABLE personal_factors (
	"Age" INT,
	"Distance from Home" INT,
	"Education" INT,
	"Education Field" VARCHAR,
	"Employee Number" INT PRIMARY KEY,
	"Gender" VARCHAR,
	"MaritalStatus" VARCHAR
	NumberCompaniesWorked INT
	Over18 VARCHAR
	RelationsSatisfaction INT
	TotalWorkingYears INT
	WorkLifeBalance INT
);

SELECT * FROM personal_factors;

--professional factors table
CREATE TABLE work_factors (
	"Business Travel" VARCHAR
	"Daily Rate" INT
	"Department" VARCHAR
	"Employee Count" INT
	EmployeeNumber INT PK
	"Environment Satisfaction" INT,
	HourlyRate INT
	JobInvolvement INT
	JobLevel INT
	JobRole VARCHAR
	JobSatisfaction INT
	MonthlyIncome INT
	MonthlyRate INT
	Overtime VARCHAR
	PercentSalaryHike INT
	PerformanceRating INT
	StandardHours INT
	StockOptionLevel INT
	TrainingTimesLastYear INT
	YearsatCompany INT
	YearsInCurrentRole INT
	YearsSinceLastPromotion INT
	YearsWithCurrentManager INT
	"Attrition" VARCHAR
);

SELECT * FROM work_factors

--total factors table