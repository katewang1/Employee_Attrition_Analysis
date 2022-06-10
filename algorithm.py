# labels textbox information
def get_features_list():
    ''' 
    The function provides labels for user textboxs.

    Parameters:
        None. 

    Returns:
        list: The list which provides variable names, textbox placeholder values, bextbox labels, and keys.
    '''
    return [
    ('age', 41,'Age', ''),
    ('business_travel', 2,'Business Travel', '1=No Travel, 2=Travel Frequently, 3=Travel Rarely'),
    ('department', 2,'Department', '1=HR, 2=R&D, 3=Sales'),
    ('distance_from_home', 1,'Distance from Home to Work',''),
    ('education_level', 2,'Education Level','1=Below College, 2=College, 3=Bachelor, 4=Master, 5=Doctor'),
    ('education_field', 1,'Education Field','1=HR, 2=Life Sciences, 3=Marketing, 4=Medical sciences, 5=Others, 6=Technical'),
    ('environment_satisfaction', 2,'Environment Satisfaction','1=Low, 2=Medium, 3=High, 4=Very High'),
    ('gender', 0,'Gender','1=Female, 2=Male'),
    ('job_involvement', 3,'Job Involvement','1=Low, 2=Medium, 3=High, 4=Very High'),
    ('job_role', 7,'Job Role','1 = HC Rep, 2=HR, 3=Lab Technician, 4=Manager, 5=Managing Director, 6=Research Director, 7=Research Scientist, 8=Sales Executieve, 9=Sales Representative'),
    ('job_satisfaction', 4,'Job Satisfaction','1=Low, 2=Medium, 3=High, 4=Very High'),
    ('marital_status', 2,'Marital Status','1=Divorced, 2=Married, 3=Single'),
    ('monthly_income', 5993,'Monthly Income',''),
    ('number_companies_worked', 8,'Number Companies Worked',''),
    ('overtime', 1,'Overtime','1=No, 2=Yes'),
    ('percent_salary_hike', 11,'Percent Increase in Salary',''),
    ('performance_rating', 3,'Performance Rating','1=Low, 2=Good, 3=Excellent, 4=Outstanding'),
    ('relationship_satisfaction', 1,'Relationship Satisfaction','1=Low, 2=Medium, 3=High, 4=Very High'),
    ('stock_option_level', 0,'Stock Option Level',''),
    ('training_times_last_year', 0,'Hours Training Last Year',''),
    ('work_life_balance', 1,'Work Life Balance','1=Bad, 2=Good, 3=Better, 4=Best'),
    ('years_at_company', 6,'Years at Company',''),
    ('years_since_last_promotion', 0,'Years Since Last Promotion','')
]

def result(pred_proba):

    '''
    The function provides the result based on user input.

    Parameters:
        pred_prob(numpy array): The variable that compares the probaility of attrition and remaining with company.

    Returns:
        result(str): The result that contains the probability percentage.
    '''

    if pred_proba[0][0] < pred_proba[0][1]:
        result = f"The model predicts with a {pred_proba[0][1] * 100:.2f}% probability that your employee WILL leave the company."
        return result
    elif pred_proba[0][0] == pred_proba[0][1]:
        result = f"The model predicts that your employee as likely to remain with the company as they are staying."
        return result
    else:
        result = f"The model predicts with {pred_proba[0][0] * 100:.2f}% probability that your employee WILL NOT leave the company."
        return result