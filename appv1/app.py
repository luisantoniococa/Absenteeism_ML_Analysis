from flask import Flask, render_template, request, redirect, session
from forms import PredictForm
import pandas as pd
import pickle


model = pickle.load(open('../application/modelForDeploy.pkl','rb'))



app = Flask(__name__)



app.config['SECRET_KEY'] = 'password'

@app.route('/')
def home():
    return 'Hello World'

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

    df = pd.DataFrame(data={'Reason_1': reason_list[0],
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
                        },index=[0])


    print(df)
    predicted_list = []
    predicted_list.append(model.predict_proba(df))
    predicted_list.append(model.predict(df))
    return render_template('predictions.html',ses = ses, predicted_list = predicted_list)

if __name__ == '__main__':
    app.run()