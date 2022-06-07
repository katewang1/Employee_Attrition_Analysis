# import dependencies
import os
import pandas as pd

def get_data():
    df = pd.read_json("data.json")
    print(df.head(5))

def label(df):

    # create dictionary with first row values from dataset
    dct = {
        "Age": df.iloc[0][0],
        "Distance From Home": df.iloc[0][4],
        "Monthly Income": df.iloc[0][14]
    }
    return dct

def get_features_list():
    return [
    ('age', 100,'Age', 'Numerical Value'),
    ('business_travel', 100,'Business Travel', '1=No Travel, 2=Travel Frequently, 3=Tavel Rarely'),
    ('department', 100,'1=HR, 2=R&D, 3=Sales'),
    ('distance_from_home', 100,'Distance from Home','Distance from work to home'),
    ('education_level', 100,'Education Level','Numerical Value'),
    ('education_field', 100,'Education Field','1=HR, 2=LIFE SCIENCES, 3=MARKETING, 4=MEDICAL SCIENCES, 5=OTHERS, 6= TEHCNICAL'),
    ('environment_satisfaction', 100,'Environment Satisfaction','Numerical Value'),
    ('gender', 100,'Gender','1=FEMALE, 2=MALE'),
    ('job_involvement', 100,'Job Involvement','Numerical Value'),
    ('job_role', 100,'Job Role','1=HC REP, 2=HR, 3=LAB TECHNICIAN, 4=MANAGER, 5= MANAGING DIRECTOR, 6= REASEARCH DIRECTOR, 7= RESEARCH SCIENTIST, 8=SALES EXECUTIEVE, 9= SALES REPRESENTATIVE'),
    ('job_satisfaction', 100,'Job Satisfaction','Numerical Value'),
    ('marital_status', 100,'Marital Status','1=DIVORCED, 2=MARRIED, 3=SINGLE'),
    ('monthly_income', 100,'Monthly Income','Monthly Salary'),
    ('number_companies_worked', 100,'Number Companies Worked',''),
    ('overtime', 100,'Overtime','1=NO, 2=YES'),
    ('percent_salary_hike', 100,'Percent Salary Hike',''),
    ('performance_rating', 100,'Performance Rating',''),
    ('relationship_satisfaction', 100,'Relationship Satisfaction',''),
    ('stock_option_level', 100,'Stock Option Level',''),
    ('training_times_last_year', 100,'Training Times Last Year','Hours spent training'),
    ('work_life_balance', 100,'Work Life Balance','Time spent between work and outside'),
    ('years_at_company', 100,'Years at Company',''),
    ('years_since_last_promotion', 100,'Years Since Last Promotion','')
]

def result(pred_proba):

    if pred_proba[0][0] < pred_proba[0][1]:
        return f"The model predicts with a {pred_proba[0][1] * 100:.2f}% probability that your employee WILL leave the company."
    elif pred_proba[0][0] == pred_proba[0][1]:
        return f"The model predicts that your employee as likely to remain with the company as they are staying."
    else:
        return f"The model predicts with {pred_proba[0][0] * 100:.2f}% probability that your employee WILL NOT leave the company."