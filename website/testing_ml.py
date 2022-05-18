# import libraries
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
# from sklearn.ensemble import RandomForestClassifier
import pickle

# read from csv; CHANGE TO DATABASE ONCE DECIDED
path = "C:/Users/gilig/Class/group_project/Employee_Attrition_Analysis/resources/IBM_employee_data.csv"
df = pd.read_csv(path)

# DROP THE AMBIGUOUS COLUMNS AND OTHER PREPROCESSING


# split data between features and target
X = df.drop(columns="Attrition")
target = ["Attrition"]
y = df.loc[:,target].copy()

# Split the preprocessed data into a training and testing dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y)

# Create a StandardScaler instances
scaler = StandardScaler()

# Fit the StandardScaler
X_scaler = scaler.fit(X_train)

# Scale the data
X_train_scaled = X_scaler.transform(X_train)
X_test_scaled = X_scaler.transform(X_test)

# Train the Logistic Regression model using the resampled data
lr_model = LogisticRegression()
lr_model.fit(X_train_scaled, y_train)

# pickling... serialization
# write to model in external model.pkl file
pickle.dump(lr_model, open("model.pkl","wb"))
