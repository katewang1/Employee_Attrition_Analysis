# The Tale of Flight Risk & the Holy Grail of Corporate Happiness
## *Predicting Employee Attrition and Exploring it's Causes*
### Link to Dashboard:
---
</br>

## Why is understanding WHEN and WHY employees quit important?

Intimately understanding employee attrition and its causes empowers organizations from any sector to retain the most skilled workers, save on costly training, and improve overall organizational culture and employee sentiment. It is also symbiotic, which is one of the biggest testaments of whether a system is successful and will last.  Focusing on employee retention benefits not just the organization’s success and longevity, but also the employees, so the system continues to feed itself.  And employee attrition affects EVERY industry.

<img align="left" src="https://github.com/Insmire/Employee_Attrition_Analysis/blob/main/resources/hard_v_soft_costs.png" width="500" />
According to the Work Institute, most of the cost from employee churn actually comes from hidden or “soft” costs, such as loss of productivity, knowledge and time.  Trading out one employee for another is not an even trade.  As you can see in the graph below, there is a significant amount of time where money is being lost before a new hire starts to produce a return for the company, and an even longer time before they can get to the level of engagement and productivity of the employee whose shoes they are filling.
</br>
</br>

When an organization loses an employee, this really equates to approximately 1.5 – 2x the previous employee’s annual salary in hard costs.  Money that could have gone into keeping the employee happy and retaining them. For hourly workers, approximately $1,500, and estimates range based on type of position and seniority.


<img align="right" src="https://github.com/Insmire/Employee_Attrition_Analysis/blob/main/resources/employee_cost_to_value.png" width="500" />
One must consider all the hard and soft costs of failing to retain valuable employees.  During the hiring process, there are costs involved with advertising job openings, interviewing and screening, time and training during onboarding, and loss of productivity, as a new person may take 1-2 years to reach the productivity of the previous employee.  Loss of business, as the new employees are less adept at problem solving and responding to issues, and may actually not even end up being a good fit for the company. Cultural impact.  Whenever someone leaves, others inherently ask why, and no one wants to go down with a sinking ship.  And the stress of understaffing can result in burnout. 
</br>
</br>

If employers were able to make a best guess at predicting when their current employees might quit and why, they may be able to intervene in time.
</br>
</br>

## Project Overview



</br>
</br>

#### Process
Our analysis and predictions can assist employers with getting to the root of employee grievances, guide management on timing for engagement with their employees, raises or role restructuring, and improve the workplace environment for the employees. (To develop further purpose based on additional dataset, widening scope to either how attrition affects the customer base or more about the employees?)
</br>
</br>

#### Findings
Briefly, we found that younger people and closer to the start of their career were more likley to leave their job.
</br>
</br>

#### Components of Project
- 3 Machine Learning Models
    - Logistic Regression
    - Random Forest
    - Neural Network

- Dashboard
    - Users can determine whether or not they are likely to stay in their current job by finding in a select number of boxes.
</br>
</br>


### Process
#### Data Source
- IBM_employee_data.csv 

#### Data Cleaning and Preparing for Machine Learning
The data came to us quite clean and not very many actions were needed to clean it. Columns with ambiguously explained data, unique identifiers, and with values that were the same throughout each rows were dropped. 

To prepare the data for machine learning, the categorical data was first encoded. There was evidence of multicollinearity, which is when 2 or more of the features are highly correlated to each other. To address this issue, four more columns were dropped. The non-encoded columns were then standardized.

![](Machine_Learning/correlation_heatmap.png)


#### Logistic Regression Model

The purpose of the model was to predict whether an employee will stay or leave their current job.  The model predicted at 75.47% accuracy. The classification report is below. 

![](resources/logReg_classificationReport.png)

#### Random Forest

we used this model both because it is good for binary classification as well as the fact that it could determine feature importance which we weould use in the exploratory analysis. it ended up with an 84% accuracy but due to the high number of false negatives we did not end up using this model.
The classification report, confusion matrix and feture importance can be seen below.

<img width="474" alt="Screen Shot 2022-06-08 at 9 22 45 PM" src="https://user-images.githubusercontent.com/39388246/172763604-93cce0e3-6191-4861-a8d3-ddfd470ceed9.png">

<img width="737" alt="Screen Shot 2022-06-08 at 9 23 05 PM" src="https://user-images.githubusercontent.com/39388246/172763631-edd181e5-919e-4dd1-8582-426409a19899.png">

<img width="113" alt="Screen Shot 2022-06-08 at 9 30 44 PM" src="https://user-images.githubusercontent.com/39388246/172764451-6616b3eb-6d6e-4492-b802-50b962920bf2.png">


#### Neural Network
The Neural network we ended with used 2 layers as well as an ouput layer. The Keras sequential model was used along with 3 layers using the sigmoid activation functoin, as it is the best for binary classification. it ended with a 87.41% accuracy with a loss of 1.97 so it performed extremely well. However given it was completed late in the process and we were unabl to get the breakdown of false positives and negatives we did not use this on the website.
</br>
</br>

### Exploratory Data Analysis
#### Findings
Using Python's seaborn library and Tableau, trends about the data were uncovered. The data is telling us that those who are more likely to leave to pursue other opportunities are younger and in the beginning their careers.

##### Age Vs. Attrition
![](Exploratory_Analysis/images/age_barplot.png)


##### Total Working Years Vs. Attrition
![](Exploratory_Analysis/images/workingYrsVSattrition.png)

##### Number of Companies Worked For Vs. Attrition
![](Exploratory_Analysis/images/NumCompaniesWorked_barplot.png)

##### Years at Company Vs. Attrition
![](Exploratory_Analysis/images/YrsAtCompany_barplot.png)
</br>
</br>

## 
While attrition is a problem that effects every industry, use of our predictive models and findings are most helpful for large-scale organizations, where individual sentiment often flies under the radar and employees fall through the cracks. 



### Software/Tools Used:
 - pgAdmin (add versions later)
- Google Collab
- Python
    - Pandas
    - Sklearn
- PostgreSQL
- AWS
- Jupyter Notebook
- VS Code
- Tableau   

##### Link to Presentation Slides
https://docs.google.com/presentation/d/1GCnuq3QFD7YBTuNLOd9c_YpS5zzCBbDL3zUX_teldi0/edit?usp=sharing
<br>

##### Citations
