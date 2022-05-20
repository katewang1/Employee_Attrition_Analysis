# Employee Attrition Prediction and Analysis
## *Predicting Attrition and Exploring Causes Based on Internal Business and Personal Factors*
### Project Overview: (explain basic project process)
---
</br>
Intimately understanding employee attrition and its causes empowers organizations from any sector to retain the most skilled workers, save on costly training, and improve overall organizational culture and employee sentiment.  While attrition is a problem that effects every industry, use of our predictive models and findings are most helpful for large-scale organizations, where individual sentiment often flies under the radar and employees fall through the cracks.  
</br>
</br>

Our analysis and predictions can assist employers with getting to the root of employee grievances, guide management on timing for engagement with their employees, raises or role restructuring, and improve the workplace environment for the employees. (To develop further purpose based on additional dataset, widening scope to either how attrition affects the customer base or more about the employees?)
</br>
</br>


### Project Outline (give me your input to change or add items as needed)
 1. Find data and form project purpose
 2. Data cleaning for DB import and preprocessing for ML model
 5. Create DB structure and import static data
 6. Perform exploratory analysis via SQL queries
 7. Set up ML model(s)
 8. Run model(s) and determine most heavily weighted attributes
 9. Utilize most heavily weighted attributes to direct focus for finding additional dataset(s)
 10. Use new dataset(s) to perform additional exploratory analysis and project purpose
 11. Asses accuracy and optimize ML model(s)
 12. Connect ML model to web page via Flask app; build web page
 13. Design Flask to take in user inputs and provide outputs, and add additional stylings for web page
 14. Continue data exploration and create graphs via Tableau
 15. Present purpose, process and findings in Tableau slide presentation
 </br>
 

### 1st Segment Deliverables (delete or work parts into other sections of readme later)

**Selected topic:** Employee Attrition

**Reason we selected topic:** Interested in looking at human behavior in a way that is business-oriented, and has a lot of room for exploratory analysis.  

**Description of dataset:** The attrition dataset is manufactured with fictional HR employee information by IBM data scientists.  It contains 1,470 instances or rows, and 35 columns or features including the target.  Features are a combination of personal employee data, answers to questionairres, employee's position-related data, and whether each employee has left the company.

**Questions we hope to answer with the data:** which features are most heavily weighted.  Can the features be categorized so that they are ranked by the order that drives the most cause for leaving? Can the employee intervene on these causes?  When can or should they intervene?  How?  Potentially how employing these interventions can improve the employee and/or client experience.

**Communication Protocols:** To use Slack channel #team-5 for group direction and questions, suggest initial tasks, request task assistance, resources, schedule group meetings.  To use Slack channel #proj-git to communicate when a given team member is working on a project/branch, inform when done with portion of project, and to request another project member look over and add comments or approve pull request.  GitHub pull request comments for suggested/requested changes to existing branch projects.  Meet by Zoom on Sundays or as needed to get on some page and discuss more complex issues and direction.
</br>
</br>

**Languages/libraries used thus far:**  
    
    python
    pandas
    matplotlib
    scikit-learn
    sql
    
</br>

**Potential machine-learning models:**
    
    supervised logistic regression - to determine whether employee is likely to leave
    supervised random forrest - to focus on feature importance
    neural network (if time)
</br>

**Database Integration:**

    PgAdmin/Postgres - import CSVs and build DB for exploratory analysis by queries
    SQLAlchemy - provisional database connection to machine learning model
    
### 2nd Segment Deliverables (delete or work parts into other sections of readme later)

**Presentation:**

    Include selected topic, reason topic was selected, description of source data and questions we hope to answer w/ the data in slides.
    Above questions answered in the 1st segment above.  Feel free to change as needed.
    ? Write and add description of the data exploration phase and description of the analysis phase of the project to slides - TBD?
    Tableau Storyboard utilized for project explanation and website built for project demonstration.
    
**Dashboard:**

    Tableau Storyboard (and website?)
    Results of each ML model within Jupyter Notebook and exploratory analysis from Postgres will be used to create the final dashboard.
    Description of interactive element(s) - TBD
    
 **GitHub**
 
    All code necessary to perform exploratory analysis - Alex, queries in the works.
    Will require additional exploration w/ additional dataset
    Some code necessary to complete ML model - need to push and merge to main/connect with preprocessing
    
**ML Model**

    Description of preliminary data preprocessing - Joey
    Description of preliminary feature engineering and feature selection, including the decision making process - Joey
    Description of how data was split into training and testing sets - Stephen
    Explanation of model choice, including limitations and benefits - Stephen
       
**Database Integration**   

    DB stores static data for use during the project - check
    DB interfaces with the project in some format - Alex
    Includes at least two tables - check
    Includes at least one join using the database language - Alex
    Includes at least one connection string (using SQLAlchemy or PyMongo) - Alex  


## Results
</br>

(Which factors were most heavily weighted?  Individually and/or by categories of sorts?  Personal, work environment, etc.  Can we improve attrition rate by adjusting the inputs?)
</br>
</br>


## Resources  
</br>

**Data Sources:**

    IBM_employee_data.csv 
    additional_dataset  

**Software:**

    pgAdmin (add versions later)
    Google Collab
    Jupyter Notebook
    VS Code
    Tableau   
</br>

## Summary
</br>
