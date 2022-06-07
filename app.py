# import dependencies
# add one for connection to aws or database
from flask import Flask, render_template, request, jsonify
import pickle
# import numpy
# from config import Config
import connection

# boilerplate; create Flask app instance
app = Flask(__name__)

# pull configuration from external config file
# app.config.from_object(Config)

# read from external pickle files
model_file = "resources/model.pkl"
model = pickle.load(open(model_file, "rb"))
scaler_file = "resources/scaler.pkl"
scaler = pickle.load(open(scaler_file, "rb"))    

# get dataframe
# connection.get_data()

# create root route 
@app.route("/", methods=["GET", "POST"])
def root():
    features_list = get_features_list()
    return render_template("index_2.html", features_list = features_list)

# create route for prediction result
@app.route("/test", methods=["GET", "POST"])
def testing():
    '''DOC STRING HERE'''
    features = request.form.getlist("features")

    # EXPLAIN THE MAGIC
    if request.method == "POST":

        # features_scaled = scaler.fit_transform(features)
        features_array=[[int(x) for x in features]]
        print("features array: ", features_array, type(features))
        pred_proba = model.predict_proba(features_array)
        print("prediction is", pred_proba, type(pred_proba))
        return jsonify(connection.result(pred_proba))

        # print(connection.label)
        # features=[[int(x) for x in features]]
        # print("features: ", features, type(features))
        # features_array=[np.array(features)]
        # print("features_array", features_array, type(features_array))
        # pred_proba = model.predict_proba(features)
        # print("prediction is", pred_proba, type(pred_proba))
        # output = "{0:.{1}f}".format(prediction[0][1], 2)
        # print("output is", output)
        # return render_template("index.html", placeholder = connection.label , pred = "Based on existing dataset the model predict that {}".format(output)) 

# create route for prediction using best
# @app.route("/pre", methods=["GET", "POST"])
# def attrition():
    
#     # variable = request.form.get("test")
#     # return f"<h1> {variable} </h1>"

#     return '''
#     <form method="POST">
#         <div><label>Test: 
#         <input type="text" name="test"></label></div>
#         <input type="submit" value="Submit" >
#     </form>
#     '''

def get_features_list():
    return [
    ('age', 100,'Age'),
    ('business_travel', 100,'Business Travel'),
    ('department', 100,'Department'),
    ('distance_from_home', 100,'Distance from Home'),
    ('education_level', 100,'Education Level'),
    ('education_field', 100,'Education Field'),
    ('environment_satisfaction', 100,'Environment Satisfaction'),
    ('gender', 100,'Gender'),
    ('job_involvement', 100,'Job Involvement'),
    ('job_role', 100,'Job Role'),
    ('job_satisfaction', 100,'Job Satisfaction'),
    ('marital_status', 100,'Marital Status'),
    ('monthly_income', 100,'Monthly Income'),
    ('number_companies_worked', 100,'Number Companies Worked'),
    ('overtime', 100,'Overtime'),
    ('percent_salary_hike', 100,'Percent Salary Hike'),
    ('performance_rating', 100,'Performance Rating'),
    ('relationship_satisfaction', 100,'Relationship Satisfaction'),
    ('stock_option_level', 100,'Stock Option Level'),
    ('training_times_last_year', 100,'Training Times Last Year'),
    ('work_life_balance', 100,'Work Life Balance'),
    ('years_at_company', 100,'Years at Company'),
    ('years_since_last_promotion', 100,'Years Since Last Promotion')
]

# boilerplate; debugger on
if __name__ == "__main__":
    app.run(debug = True)
