# import libraries
# add one for connection to aws or database
# REMOVE JSONIFY
from flask import Flask, render_template, request, jsonify
# import pickle
# NUMPY NECESSARY?
import numpy as np

# boilerplate; create Flask app instance
app = Flask(__name__)

# read from external model.pkl file
# model=pickle.load(open("model.pkl","rb"))

# create root route
@app.route("/")
def hello_world():
    hello_dict = {"say_hello": "hello beautiful ;) "}
    return hello_dict

# create route for logistic regression ml model prediction
@app.route("/attrition/logistic_regression") #, method=["POST", "GET"])
def lr():
    features=request.form.values()
    # print(features)
    return features

# create route for random forest ml model prediction
# @app.route("/attrition/random_forest")
# def rf():

#     return jsonify()

# boilerplate; debugger on
if __name__ == "__main__":
    app.run(debug = True)