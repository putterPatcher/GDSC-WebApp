import solara
from components.buttons import CellLineButton
from components.form import PredictForm
import json

with open('models/x_t2.json', 'r') as file:
    input_label = solara.reactive(json.loads(file.read()))

input_value = solara.reactive([solara.reactive(0) for _ in range(len(input_label.value))])
x = "Gene"
output_value = solara.reactive('')
disable = solara.reactive(False)
disable_random = solara.reactive(False)

import joblib
model = joblib.load('models/table_2.joblib')
encoder = joblib.load('models/y_2.joblib')
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

max_value = solara.reactive(1.0)
min_value = solara.reactive(0.0)
close_zero_count = solara.reactive(263)
zero_max_value = solara.reactive(0.4)

def fill_random_values():
    disable_random.value = True
    pos = [random.randrange(0, len(input_label.value)) for _ in range(close_zero_count.value)]
    for i in range(len(input_label.value)):
        if i not in pos:
            input_value.value[i].value = random.uniform(min_value.value, max_value.value)
        else:
            input_value.value[i].value = random.uniform(0.006, zero_max_value.value)
    disable_random.value = False

@solara.component
def DNAMethylation():
    CellLineButton()
    solara.Text("DNA Methylation (Gaussian Naive Bayes)", style='margin-top:1rem;font-size:1.2rem;')
    solara.Text('Prediction: {}'.format(output_value.value), style='padding-top:1rem')
    with solara.Div(style='text-align: center;display: flex;justify-content: space-between; align-items: center'):
        solara.Button('Random', on_click=fill_random_values, color='indigo', style='color:white; width:7rem', disabled=disable_random.value)
        with solara.Div(style='text-align: center;display: flex;gap: 3rem; align-items: center'):
            solara.InputInt("Close to zero ({} max)".format(len(input_label.value)), value=close_zero_count)
            solara.InputFloat("Close to zero upper limit".format(len(input_label.value)), value=zero_max_value)
            solara.InputFloat("Min", value=min_value)
            solara.InputFloat("Max", value=max_value)
    PredictForm(input_value, input_label, predict_output, x, disable)