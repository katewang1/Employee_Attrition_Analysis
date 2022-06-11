# import dependencies
from flask import Flask, render_template, request, jsonify, redirect
import pickle
import algorithm
from os import getenv
# from pprint import pprint

# Load environment variables
load_dotenv()

# boilerplate; create Flask app instance
app = Flask(__name__)

# Get the connection string for the database
app.config['aws_rds'] = getenv('aws_rds', '')

# retrieve model from external file
model_file = "resources/model.pkl"
model = pickle.load(open(model_file, "rb"))   

# create root route
@app.route("/", methods=["GET", "POST"])
def pred():

    '''
    The function presents user with front page of app and retrieve user input.
    
    Parameters:
        get_features_list: The function that consists of variable name, example value, variable shown in brower, and key for input.
    
    Returns:
        html: The homepage which contains textboxes for user input.
    '''

    features_list = algorithm.get_features_list()
    return render_template("index_3.html", features_list = features_list)

# create route for prediction result
@app.route("/process", methods=["GET", "POST"])
def process():

    '''
    The function takes in user input and uses model to predict the probability of attrition.

    Parameters:
        get_features_list: The function which each feature of user input is assigned to the corresponding variable.

    Returns:
        result_string(str): The variable that utilizes the result function to make a prediction based on model after features are converted to an array. 
    '''

    feature_dict = {}
    features_list = algorithm.get_features_list()
    for feature in features_list:
        feature_dict[feature[0]] = request.form[feature[0]]
    # pprint(feature_dict)
    if request.method == "POST":
        features_array=[[int(x) for x in feature_dict.values()]]
        # print("features_array is ", features_array, type(features_array))
        pred_proba = model.predict_proba(features_array)
        # print("prediction is", pred_proba, type(pred_proba))
        result_string = algorithm.result(pred_proba)
        # print(result_string)
        return jsonify(result_string)
    
    ## redirect to homepage
    return redirect('/', code=302)

# boilerplate; debugger on
if __name__ == "__main__":
    app.run(debug = True)
