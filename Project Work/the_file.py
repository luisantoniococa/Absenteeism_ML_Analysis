import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
from absenteeism_module import *

model = absenteeism_model('model','scaler')