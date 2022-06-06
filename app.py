# import libraries
# add one for connection to aws or database
from flask import Flask, render_template, request, jsonify
import pickle
import numpy as np
from config import Config, secret
import connection

# boilerplate; create Flask app instance
app = Flask(__name__)

# pull configuration from external config file
app.config.from_object(Config)

# read from external pickle files
# model_file = "resources/model.pkl"
# model = pickle.load(open(model_file, "rb"))
# scaler_file = "resources/scaler.pkl"
# scaler = pickle.load(open(scaler_file, "rb"))    

# get dataframe
# connection.get_data()

# create root route 
@app.route("/", methods=["GET", "POST"])
def root():
    return render_template("index.html")

# create route for prediction result
@app.route("/test", methods=["GET", "POST"])
def testing():
    '''DOC STRING HERE'''
    features = request.form.getlist("features")

    # EXPLAIN THE MAGIC
    if request.method == "POST":

        model = connection.get_model()
        # SCALE DATA?
        features=[[int(x) for x in features]]
        print("features: ", features, type(features))
        pred_proba = model.predict_proba(features)
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

# boilerplate; debugger on
if __name__ == "__main__":
    app.run(debug = True)
