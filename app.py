from flask import Flask, request, render_template
from templates.languages import languages
import pandas as pd
import tensorflow as tf
from templates.headers import headers

# import pickle
# import numpy as np
# from sklearn.linear_model import LogisticRegression
# from sklearn.model_selection import train_test_split
# import pandas as pd


app = Flask(__name__)

model = tf.keras.models.load_model('dnn_model/.')

# @app.route('/')
# def my_form():
    
#     return render_template('test1.html')

@app.route('/', methods=['POST', 'GET'])
def model_prediction():
    testlist = languages
    salary = [[""]]
    params = []
    years = ""
    langs = []

    if request.method == 'POST':
        list = []
        years = float(request.form.get('CodingPro'))
        list.append(years)
        langs = (request.form.getlist('checkbox'))
        print(langs)
        params = [int(i in langs) for i in testlist] 
        list = list + params
        print(list) 
        print(list[0])
        prediction_list = pd.DataFrame([list], columns = headers)

        salary = model.predict(prediction_list)

    return render_template('test1copy.html', pred=salary[0][0], selections=langs, yearsCoding=years)

if __name__ == '__main__':
    app.run(debug=True)

