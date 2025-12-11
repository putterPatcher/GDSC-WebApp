import solara
from components.buttons import HomeButton
import joblib

x_rf3 = joblib.load('models/x_rf3.joblib')
x_rf1 = joblib.load('models/x_rf1.joblib')
y_cell_line = joblib.load('models/y_cell_line.joblib')

model_gb1 = joblib.load('models/gb1.joblib')
model_gb3 = joblib.load('models/gb3.joblib')
model_rf1 = joblib.load('models/rf1.joblib')
model_rf3 = joblib.load('models/rf3.joblib')

input_type = ['text', 'text', 'text']
value_cancertype = solara.reactive('ACC')
value_medium = solara.reactive('R')
value_growth = solara.reactive('Adherent')
output_value = solara.reactive('')
model = solara.reactive('Gradient Boost (1 Variable)')
models = ['Gradient Boost (1 variable)', 'Random Forest (1 variable)', 'Gradient Boost (3 variables)', 'Random Forest (3 variables)']

cancer_types = ['ACC', 'ALL', 'BLCA', 'BRCA', 'CESC', 'CLL', 'COAD/READ', 'DLBC',
       'ESCA', 'GBM', 'HNSC', 'KIRC', 'LAML', 'LCML', 'LGG', 'LIHC',
       'LUAD', 'LUSC', 'MB', 'MESO', 'MM', 'NB', 'OV', 'PAAD', 'PRAD',
       'SCLC', 'SKCM', 'STAD', 'THCA', 'UCEC', 'UNABLE TO CLASSIFY']
screen_medium = ['D/F12', 'R']
growth_properties = ['Adherent', 'Semi-Adherent', 'Suspension']
categories = ['Cancer Type (matching TCGA label)', 'Screen Medium', 'Growth Properties']

def predict_output():
    output_value.value = ''
    if model.value == 'Gradient Boost (3 variables)':
        df = pd.DataFrame()
        df[categories[0]] = [value_cancertype.value, ]
        df[categories[1]] = [value_medium.value, ]
        df[categories[2]] = [value_growth.value, ]
        output_value.value = y_cell_line.inverse_transform(model_gb3.predict(df))[0]
    elif model.value == 'Random Forest (3 variables)':
        df = pd.DataFrame()
        df[categories[0]] = [value_cancertype.value, ]
        df[categories[1]] = [value_medium.value, ]
        df[categories[2]] = [value_growth.value, ]
        output_value.value = y_cell_line.inverse_transform(model_rf3.predict(x_rf3.transform(df)))[0]
    elif model.value == 'Random Forest (1 variable)':
        df = pd.DataFrame()
        df[categories[0]] = [value_cancertype.value, ]
        output_value.value = y_cell_line.inverse_transform(model_rf1.predict(x_rf1.transform(df)))[0]
    elif model.value == 'Gradient Boost (1 variable)':
        df = pd.DataFrame()
        df[categories[0]] = [value_cancertype.value, ]
        output_value.value = y_cell_line.inverse_transform(model_gb1.predict(df))[0]

import pandas as pd

@solara.component
def MSI():
    HomeButton()
    solara.Select(label="Model", value=model, values=models)
    solara.Text("Prediction: {}".format(output_value.value))
    if model.value in models:
        with solara.Row(justify='center'):
            solara.Button("Predict", on_click=predict_output, style='color:white;background-color:black;width:15rem;')
    match model.value:
        case 'Gradient Boost (1 variable)':
            solara.Select(label="Cancer Type (matching TCGA label)", values=cancer_types, value=value_cancertype)
        case 'Random Forest (1 variable)':
            solara.Select(label="Cancer Type (matching TCGA label)", values=cancer_types, value=value_cancertype)
        case 'Gradient Boost (3 variables)':
            solara.Select(label="Cancer Type (matching TCGA label)", values=cancer_types, value=value_cancertype)
            solara.Select(label='Screen Medium', values=screen_medium, value=value_medium)
            solara.Select(label='Growth Properties', values=growth_properties, value=value_growth)
        case 'Random Forest (3 variables)':
            solara.Select(label="Cancer Type (matching TCGA label)", values=cancer_types, value=value_cancertype)
            solara.Select(label='Screen Medium', values=screen_medium, value=value_medium)
            solara.Select(label='Growth Properties', values=growth_properties, value=value_growth)
        case _:
            solara.Error("Incorrect Model")