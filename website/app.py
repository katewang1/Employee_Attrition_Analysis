# import libraries
# add one for connection to aws or database
from flask import Flask, render_template, request
import pickle
import numpy as np

# boilerplate; create Flask app instance
app = Flask(__name__)

# read from external model.pkl file
model=pickle.load(open("model.pkl","rb"))

# create root route
@app.route("/")
def root():
    return render_template("index.html")

# create route for logistic regression ml model prediction
@app.route("/attrition/logistic_regression", methods=["POST", "GET"])
def lr():
    features=[request.form.values()]
    features_array=[np.array(features)]
    prediction = model.predict_prob(features_array)
    output = "{0:.{1}f}".format(prediction[0][1], 2)
    
    return render_template("index.html", pred = "Based on the Logistic Regression model, probability of your employee leaving the company is {}".format(output))
    
    # ANDREW GAVE ME THE NEXT 9 LINES; WHOEVER TOUCHES IT DIES >:) 
    if request.method == "POST":
        variable = request.form.get("test")
        return f"<h1> {variable} </h1>"
    return '''
    <form method="POST">
        <div><label>Test: <input type="text" name="test"></label></div>
        <input type="submit" value="Submit" >
    </form>
    '''

# create route for random forest ml model prediction
# @app.route("/attrition/random_forest")
# def rf():

#     return jsonify()

# boilerplate; debugger on
if __name__ == "__main__":
    app.run(debug = True)