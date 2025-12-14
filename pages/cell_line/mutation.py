import solara
from components.buttons import CellLineButton
from components.form_binary import PredictForm
import json

with open('models/x_t3.json', 'r') as file:
    input_label = solara.reactive(json.loads(file.read()))
input_value = solara.reactive([solara.reactive(0) for _ in range(len(input_label.value))])
x = "Features"
output_value = solara.reactive('')
disable = solara.reactive(False)
disable_random = solara.reactive(False)

import joblib
model = joblib.load('models/table_3.joblib')
encoder = joblib.load('models/y_3.joblib')
import pandas as pd

def predict_output():
    disable.value = True
    output_value.value = ''
    df = pd.DataFrame()
    for i in range(len(input_label.value)):
        df = pd.concat([df, pd.DataFrame({input_label.value[i]: [input_value.value[i].value, ]})], axis=1)
    output_value.value = encoder.inverse_transform(model.predict(df))[0]
    disable.value = False

import random

def fill_random_values():
    disable_random.value = True
    pos = [random.randrange(0, len(input_label.value)) for _ in range(zero_value.value)]
    for i in range(len(input_label.value)):
        if i not in pos:    
            input_value.value[i].value = random.randint(0, 1)
        else:
            input_value.value[i].value = 0
    disable_random.value = False

zero_value = solara.reactive(128)

@solara.component
def Mutation():
    CellLineButton()
    solara.Text("Gene Mutations (Bernoulli Naive Bayes)", style='margin-top:1rem;font-size:1.2rem;')
    solara.Text('Prediction: {}'.format(output_value.value), style='padding-top:1rem')
    with solara.Div(style='text-align: center;display: flex;justify-content: space-between; align-items: center'):
        solara.Button('Random', on_click=fill_random_values, color='indigo', style='color:white; width:7rem', disabled=disable_random.value)
        with solara.Div(style='text-align: center;display: flex;gap: 3rem; align-items: center'):
            solara.InputInt("Zeros ({} max)".format(len(input_label.value)), value=zero_value)
    PredictForm(input_value, input_label, predict_output, x, disable)