import pandas as pd
# import numpy as np
# from sklearn.linear_model import LogisticRegression
# from sklearn import metrics
# from sklearn.base import BaseEstimator, TransformerMixin
# from sklearn.preprocessing import StandardScaler
# from sklearn.model_selection import train_test_split
import pickle
model = pickle.load(open('../application/modelForDeploy.pkl','rb'))

reason = float(input('Please select a reason of absence 1 tp 4 '))
month = float(input('please import the month '))
transportation = float(input('please import the transportation '))
age = float(input('please set your age '))
body = float(input('body mass index '))
education = float(input('hiest level of education '))
children = float(input('how many children '))
pets = float(input('how many pets do you have '))

# reason_list = None
if int(reason) == 1: reason_list = [1,0,0,0]
if int(reason) == 2: reason_list = [0,1,0,0]
if int(reason) == 3: reason_list = [0,0,1,0]
if int(reason) == 4: reason_list = [0,0,0,1]

df = pd.DataFrame(data={'Reason_1': reason_list[0],
                        'Reason_2': reason_list[1],
                        'Reason_3': reason_list[2],
                        'Reason_4': reason_list[3],
                        'Month Value': (month-6.36)/3.50501,
                        'Transportation Expense': (transportation-222.347143)/66.312960,
                        'Age': (age-36.417143)/6.379083,
                        'Body Mass Index': (body-26.737143)/4.254701,
                        'Education':education,
                        'Children': (children-1.021429)/1.112215,
                        'Pets': (pets-0.687143)/1.166095
                        },index=[0])

print(df)


predicted = model.predict_proba(df)
uni_pred = model.predict(df)
print(predicted)
print(f"this is the prediction {uni_pred}")