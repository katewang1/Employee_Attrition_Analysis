# import dependencies
import os
import pandas as pd
import numpy as np
# from getpass import getpass
# import sqlalchemy
# from sqlalchemy.ext.automap import automap_base
# from sqlalchemy.orm import Session
from sqlalchemy import create_engine
# , func
# from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from imblearn.over_sampling import RandomOverSampler
from sklearn.metrics import balanced_accuracy_score
import pickle
from config import secret

# def train_model():
    
#     # connect to database
#     # secret = getpass('Enter the secret value: ')
#     args ={
#         'host':"ogdataset.c11hekhsylui.us-west-1.rds.amazonaws.com",
#         'port':'5432',
#         'database':"og_dataset",
#         'user':"attritionProject",
#         'password': secret
#     }
#     engine = create_engine("postgresql://{user}:{password}@{host}/{database}".format(**args))
#     connection = engine.connect()

#     #reflect existing database into new model
#     df=pd.read_sql('SELECT * FROM new_encoded_data', connection)

#     # split data between features and target
#     # X = df[["Age", "Distance from Home", "Monthly Income"]].values
#     X = df.drop("Attrition",1).values
#     y = df["Attrition"].values
#     # target = ["Attrition"]
#     # y = df.loc[:,target].copy()

#     # Split the preprocessed data into a training and testing dataset
#     X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y)

#     # Create a StandardScaler instances
#     # scaler = StandardScaler()

#     # Fit the StandardScaler
#     # X_scaler = scaler.fit(X_train)

#     # Scale the data
#     # X_train_scaled = X_scaler.transform(X_train)
#     # X_test_scaled = X_scaler.transform(X_test)

#     # Using random oversampling increase the number of minority class (Yes values)
#     ros = RandomOverSampler(random_state=1)
#     X_resampled, y_resampled = ros.fit_resample(X_train, y_train)

#     # Train the Logistic Regression model using the resampled data
#     # CHANGE Y FROM COLUMN-VECTOR TO 1D ARRAY W/ ravel()!!! (.values yields numpy array, .ravel changes shape to (n,))
#     model = LogisticRegression()
#     # model.fit(X_train_scaled, y_train.values.ravel())
#     model.fit(X_resampled, y_resampled)

#     # pickling... serialization
#     # write to model in external model.pkl file
#     model_file = "resources/model.pkl"
#     pickle.dump(model, open(model_file, "wb"))

#     # scaler_file = "resources/scaler.pkl"
#     # pickle.dump(scaler, open(scaler_file, "wb"))

# def get_model():
#     # read from external pickle files
#     model_file = "resources/model.pkl"
#     if not os.path.exists(model_file):
#         train_model()
#     return pickle.load(open(model_file, "rb"))
#     # scaler_file = "resources/scaler.pkl"
#     # scaler = pickle.load(open(scaler_file, "rb"))    

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

def result(pred_proba):

    if pred_proba[0][0] < pred_proba[0][1]:
        return f"The model predicts that your employee will leave the company with a {pred_proba[0][1] * 100:.2f}% probability."
    elif pred_proba[0][0] == pred_proba[0][1]:
        return f"The model predicts that your employee as likely to remain with the company as they are staying."
    else:
        return f"The model predicts that your employee will NOT leave the company with {pred_proba[0][0] * 100:.2f}% probability."