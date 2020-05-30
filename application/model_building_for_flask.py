import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn import metrics
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
import pickle

data_preprocessed = pd.read_csv('../Project Work/Absenteeism_preprocessed.csv')

targets = np.where(data_preprocessed['Absenteeism Time in Hours'] > 
                   data_preprocessed['Absenteeism Time in Hours'].median(), 1, 0)

''
data_preprocessed['Excessive Absenteeism'] = targets

# print(targets.sum()/(targets.shape[0]))

data_with_targets = data_preprocessed.drop(['Absenteeism Time in Hours','Day of the week', 'Distance to Work', 
                                            'Daily Work Load Average'], axis = 1)

unscaled_inputs = data_with_targets.iloc[:,:-1]



class CustomScaler(BaseEstimator, TransformerMixin):
    
    def __init__(self,columns, copy = True, with_mean = True, with_std=True):
        self.scaler = StandardScaler(copy,with_mean,with_std)
        self.columns = columns
        self.mean_ = None
        self.var_ = None
    
    def fit(self, X, y=None):
        self.scaler.fit(X[self.columns], y)
        self.mean_ = np.mean(X[self.columns])
        self.var_ = np.var(X[self.columns])
        return self
    
    def transform(self, X, y=None, copy=None):
        init_col_order = X.columns
        X_scaled = pd.DataFrame(self.scaler.transform(X[self.columns]),columns = self.columns)
        X_not_scaled = X.loc[:,~X.columns.isin(self.columns)]
        return pd.concat([X_not_scaled, X_scaled], axis=1)[init_col_order]

columns_to_omit = ['Reason_1', 'Reason_2', 'Reason_3', 'Reason_4','Education']

columns_to_scale = [x for x in unscaled_inputs.columns.values if x not in columns_to_omit]

absenteeism_scaler = CustomScaler(columns_to_scale)

absenteeism_scaler.fit(unscaled_inputs)

scaled_inputs = absenteeism_scaler.transform(unscaled_inputs)



x_train, x_test, y_train, y_test = train_test_split(scaled_inputs, targets,train_size = 0.8,random_state = 20)

print(x_train.shape,y_train.shape)

print(x_test.shape, y_test.shape)

reg = LogisticRegression()

reg.fit(x_train,y_train)

model_outputs = reg.predict(x_train)

# checkin = (model_outputs == y_train)
# print (checkin)

print (f'intercept {reg.intercept_}')
print (f'coef_ {reg.coef_}')

print (f'test score {reg.score(x_test, y_test)}')

# Saving model to disk
pickle.dump(reg, open('modelForDeploy.pkl','wb'))

# Loading model to compare the results
# model = pickle.load(open('modelForDeploy.pkl','rb'))

# rows below help to check if the model was saved propertly
# predicted_proba = reg.predict_proba(x_test)
# predicted_proba2 = model.predict_proba(x_test)
# print(predicted_proba)
# print('-------')
# print(predicted_proba2)