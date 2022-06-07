# import dependencies
from flask import Flask, render_template, request, jsonify
import pickle
import connection
from pprint import pprint

# boilerplate; create Flask app instance
app = Flask(__name__)

# read from external pickle files
model_file = "resources/model.pkl"
model = pickle.load(open(model_file, "rb"))   

# get dataframe
# connection.get_data()

# create root route 
@app.route("/", methods=["GET", "POST"])
def root():
    features_list = connection.get_features_list()
    return render_template("index_2.html", features_list = features_list)

# create route for prediction result
@app.route("/result", methods=["GET", "POST"])
def testing():
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
        return jsonify(connection.result(pred_proba))

# boilerplate; debugger on
if __name__ == "__main__":
    app.run(debug = True)
