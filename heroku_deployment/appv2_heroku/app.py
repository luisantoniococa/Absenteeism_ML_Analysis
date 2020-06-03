from flask import Flask, render_template, request, redirect, session
from forms import PredictForm
import pandas as pd
import pickle
from flask_bootstrap import Bootstrap

# use this for windows testing and building
model = pickle.load(open('modelForDeploy.pkl','rb'))
# use this for deployment in linux
# model = pickle.load(open('/tmp/appv1/modelForDeploy.pkl','rb'))



app = Flask(__name__)

Bootstrap(app)


app.config['SECRET_KEY'] = 'password'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['GET','POST'])
def pred():
    form = PredictForm()
    if form.is_submitted():
        session['form_data'] = request.form
        # for key,value in result.items():
        #     print(f'this is the key {key} and this is the value {value}')
        print(session)
        return redirect('/prediction')
    return render_template('predict.html', form=form)
    # return redirect('/')

@app.route('/prediction')
def value_predicted():
    ses = session['form_data']
    if int(ses['reason']) == 1: reason_list =[1,0,0,0]
    elif int(ses['reason']) == 2: reason_list =[0,1,0,0]
    elif int(ses['reason']) == 3: reason_list =[0,0,1,0]
    elif int(ses['reason']) == 4: reason_list =[0,0,0,1]

    if ses['education'] == 'GED': education = 0
    else: education = 1

    data_form = {'Reason_1': reason_list[0],
                        'Reason_2': reason_list[1],
                        'Reason_3': reason_list[2],
                        'Reason_4': reason_list[3],
                        'Month Value': (int(ses['month'])-6.36)/3.50501,
                        'Transportation Expense': (int(ses['transportation'])-222.347143)/66.312960,
                        'Age': (int(ses['age'])-36.417143)/6.379083,
                        'Body Mass Index': (int(ses['body'])-26.737143)/4.254701,
                        'Education':education,
                        'Children': (int(ses['children'])-1.021429)/1.112215,
                        'Pets': (int(ses['pets'])-0.687143)/1.166095
                        }
    df = pd.DataFrame(data=data_form,index=[0])


    print(df)
    print(ses)
    predicted_list = []
    predicted_list.append(model.predict_proba(df))
    predicted_list.append(model.predict(df))
    return render_template('predictions.html',ses = ses, predicted_list = predicted_list, data_form = data_form)

# <a class="dropdown-item" href="exploration">Exploratory Data Analysis</a>
#             <a class="dropdown-item" href="model-building">Model Building</a>
#             <a class="dropdown-item" href="container">Container Development</a>
#             <a class="dropdown-item" href="cluster-deploy">Cluster Deployment</a>



@app.route('/exploration')
def exploration():
    return render_template('exploration.html')

@app.route('/model-building')
def modelBuilding():
    return render_template('modelbuilding.html')

@app.route('/container')
def container():
    return render_template('container.html')

@app.route('/cluster-deploy')
def clusterDeploy():
    return render_template('cluster.html')

@app.route('/retreival')
def dataretreival():
    return render_template('retreival.html')


if __name__ == '__main__':
    app.run(host="0.0.0.0",port="5001",debug=True)