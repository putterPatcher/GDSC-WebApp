import solara
from components.buttons import DrugButton
from components.form_binary import PredictForm
import json

with open('models/x_t9_FP.json', 'r') as file:
    input_label = solara.reactive(json.loads(file.read()))
input_value = solara.reactive([0 for _ in range(len(input_label.value))])
x = "Features"
output_value = solara.reactive('')
disable = solara.reactive(False)
disable_random = solara.reactive(False)

import joblib
model = joblib.load('models/table_9_FP.joblib')
encoder = joblib.load('models/y_9_FP.joblib')
import pandas as pd

def predict_output():
    disable.value = True
    output_value.value = ''
    df = pd.DataFrame()
    for i in range(len(input_label.value)):
        df = pd.concat([df, pd.DataFrame({input_label.value[i]: [input_value.value[i], ]})], axis=1)
    output_value.value = encoder.inverse_transform(model.predict(df))[0]
    disable.value = False

import random

zero_value = solara.reactive(384)

def fill_random_values():
    disable_random.value = True
    pos = [random.randrange(0, len(input_label.value)) for _ in range(zero_value.value)]
    input_value.value = [random.randint(0,1) if i not in pos else 0 for i in range(len(input_label.value))]
    disable_random.value = False

@solara.component
def FP():
    DrugButton()
    solara.Text("FP (Bernoulli Naive Bayes)", style='margin-top:1rem;font-size:1.2rem;')
    solara.Text('Prediction: {}'.format(output_value.value), style='padding-top:1rem')
    with solara.Div(style='text-align: center;display: flex;justify-content: space-between; align-items: center'):
        solara.Button('Random', on_click=fill_random_values, color='indigo', style='color:white; width:7rem', disabled=disable_random.value)
        with solara.Div(style='text-align: center;display: flex;gap: 3rem; align-items: center'):
            solara.InputInt("Zeros ({} max)".format(len(input_label.value)), value=zero_value)
    PredictForm(input_value, input_label, predict_output, x, disable)