import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
from absenteeism_module import *
from sklearn.preprocessing import StandardScaler
from sklearn.base import BaseEstimator, TransformerMixin

model = absenteeism_model('model','scaler')

class FactorExtractor(transformerMixin, BaseEstimator):
    def __init__(self, factor):
        self.factor = factor

    def transform(self,data):
        return data[self.factor]
    
    def fit(self, *_):
        return self

