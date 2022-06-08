# import dependencies
from flask import Flask, render_template, request, jsonify, redirect
import pickle
import connection
from pprint import pprint

# boilerplate; create Flask app instance
app = Flask(__name__)

# read from external pickle files
model_file = "resources/model.pkl"
model = pickle.load(open(model_file, "rb"))   

# create root route 
@app.route("/", methods=["GET", "POST"])
def pred():
    features_list = connection.get_features_list()
    return render_template("index_1.html", features_list = features_list)

# create route for prediction result
@app.route("/process", methods=["GET", "POST"])
def process():
    '''DOC STRING HERE'''

    feature_dict = {}
    features_list = connection.get_features_list()
    for feature in features_list:
        feature_dict[feature[0]] = request.form[feature[0]]
    pprint(feature_dict)

    # EXPLAIN THE MAGIC
    if request.method == "POST":

        features_array=[[int(x) for x in feature_dict.values()]]
        # print("features array: ", features_array, type(features_array))
        pred_proba = model.predict_proba(features_array)
        # print("prediction is", pred_proba, type(pred_proba))
        result_string = jsonify(connection.result(pred_proba))
        # return render_template("index_2.html", result_string)
        return render_template("result.html", result = result_string)
    
    ## redirect to homepage after process data
    return redirect('/', code=302)

# boilerplate; debugger on
if __name__ == "__main__":
    app.run(debug = True)
