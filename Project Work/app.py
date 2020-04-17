import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
from absenteeism_module import *
app = Flask(__name__)
model = pickle.load(open('modelForDeploy.pkl', 'rb'))
# model = absenteeism_module('model','scaler')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    int_featuresr = []
    for x in request.form.values():
        try:
            int_featuresr.append(int(x))
        except ValueError:
            int_featuresr.append(x)

    # int_featuresr = [int(x) for x in request.form.values()]
    # int_featuresr
    # int_features = [0,0,0,1,7,'1',289,'36',33,'239.554',30,0,2,1,'4']
    int_features = [0,0,0,1,-0.388293,1.036026,0.562059,-0.408580,0,-0.019280,0.268487]
    # int_features = [0,0,0,1,7,1,289,36,33,239.554,30,0,2,1,4]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)

    output = prediction[0]

    return render_template('index.html', prediction_text='Employee Salary should be $ {}'.format(output), int_features= 'This {}'.format(int_featuresr))

@app.route('/predict_api',methods=['POST'])
def predict_api():
    '''
    For direct API calls trought request
    '''
    data = request.get_json(force=True)
    prediction = model.predict([np.array(list(data.values()))])

    output = prediction[0]
    return jsonify(output)

if __name__ == "__main__":
    app.run(debug=True)