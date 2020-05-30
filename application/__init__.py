import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
# import pandas as pd
from Project Work /absenteeism_module import *
app = Flask(__name__)
# model = pickle.load(open('modelForDeploy.pkl', 'rb'))
model = absenteeism_model('model','scaler')
# count = 0

from application import routes

if __name__ == "__main__":
    app.run(debug=True)