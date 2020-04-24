import numpy as np
from flask import Flask, request, jsonify, render_template
import json
import pickle


app = Flask(__name__)
model = pickle.load(open('xgb_model.pkl', 'rb'))


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['GET', 'POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    #print(request.data)
    data = request.get_json(force = True)
    print(data.keys(),data.values())
    prediction = model.predict([np.array(list(data.values()))])
    output = round(prediction[0])
    return str(output)
    #return render_template('index.html', prediction_text='House Price is $ {}'.format(output))



    

@app.route('/predict_api',methods=['GET'])
def predict_api():
    '''
    For direct API calls through request
    '''
    data = request.get_json(force=True)
    print(data.values())
    prediction = model.predict([np.array(list(data.values()))])
    output = prediction[0]
    print(output)
    return str(output)

if __name__ == "__main__":
    app.run(debug=True)
    
#, use_reloader=False

