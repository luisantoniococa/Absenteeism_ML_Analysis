from application import app


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
    # int_features = [0,0,0,1,-0.388293,1.036026,0.562059,-0.408580,0,-0.019280,0.268487]
    # int_features = [0,0,0,1,7,1,289,36,33,239.554,30,0,2,1,4]
    # 0.87 1 
    # int_featuresr = [14,23,'06/06/2018',155,12,34,237.656,25,1,2,0]
    int_featuresr = 'Absenteeism_new_data.csv'
    # int_featuresr = pd.read_csv(int_featuresr)
    # int_featuresr = int_featuresr.iloc[count:count+1]
    model.load_and_clean_data(int_featuresr)
    # final_features = [np.array(int_features)]
    # prediction = model.predicted_output_category(final_features)
    prediction = model.predicted_output_category()
    print('*******')
    print('*******')
    print(prediction)
    print('*******')
    print('*******')
    output = prediction
    proba = model.predicted_probability()
    print(proba)
    print('*******')
    print('*******')
    # count += 1
    # print(f'the count {count}')
    return render_template('index.html', prediction_text='this  ---{}---'.format(output), 
                                        int_features= '\n the read array {}'.format(int_featuresr),
                                        probability='\n The probability for this to hapen is {}'.format(proba))

@app.route('/predict_api',methods=['POST'])
def predict_api():
    '''
    For direct API calls trought request
    '''
    data = request.get_json(force=True)
    prediction = model.predict([np.array(list(data.values()))])

    output = prediction[0]
    return jsonify(output)