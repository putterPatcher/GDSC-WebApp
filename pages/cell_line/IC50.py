import solara
from components.buttons import CellLineButton
from components.form import PredictForm
input_label = solara.reactive(['BMS-536924', 'GSK269962A', 'Doxorubicin', 'Etoposide', 'Gemcitabine', 'Mitomycin-C', 'Vinorelbine ', 'NSC-87877', 'Bicalutamide', 'QS11', 'CP466722', 'Midostaurin', 'CHIR-99021', 'Ponatinib', 'AZD6482', 'JNK-9L', 'PF-562271', 'HG6-64-1', 'JQ1', 'JQ12', 'DMOG', 'FTI-277', 'OSU-03012', 'Shikonin', 'AKT inhibitor VIII', 'Embelin', 'FH535', 'PAC-1', 'IPA-3', 'GSK650394', 'BAY-61-3606', '5-Fluorouracil', 'Thapsigargin', 'Obatoclax Mesylate', 'BMS-754807', 'Linsitinib', 'Bexarotene', 'LFM-A13', 'GW-2580', 'Luminespib', 'Phenformin', 'Bryostatin 1', 'Pazopanib', 'Dacinostat', 'Epothilone B', 'GSK1904529A', 'BMS-345541', 'Tipifarnib', 'Avagacestat', 'Ruxolitinib', 'AS601245', 'Ispinesib Mesylate', 'TL-2-105', 'AT-7519', 'TAK-715', 'BX-912', 'ZSTK474', 'AS605240', 'Genentech Cpd 10', 'GSK1070916', 'Enzastaurin', 'GSK429286A', 'FMK', 'QL-XII-47', 'Idelalisib', 'UNC0638', 'Cabozantinib', 'WZ3105', 'XMD14-99', 'Quizartinib', 'CP724714', 'JW-7-24-1', 'NPK76-II-72-1', 'STF-62247', 'NG-25', 'TL-1-85', 'VX-11e', 'FR-180204', 'Tubastatin A', 'Zibotentan', 'Sepantronium bromide', 'NSC-207895', 'VNLG/124', 'AR-42', 'CUDC-101', 'Belinostat', 'I-BET-762', 'CAY10603', 'Linifanib', 'BIX02189', 'Alectinib', 'Pelitinib', 'Omipalisib', 'KIN001-236', 'KIN001-244', 'WHI-P97', 'KIN001-260', 'KIN001-266', 'Masitinib', 'Amuvatinib', 'MPS-1-IN-1', 'NVP-BHG712', 'OSI-930', 'OSI-027', 'CX-5461', 'PHA-793887', 'PI-103', 'PIK-93', 'SB52334', 'TPCA-1', 'Fedratinib', 'Foretinib', 'Y-39983', 'YM201636', 'Tivozanib', 'GSK690693', 'SNX-2112', 'QL-XI-92', 'XMD13-2', 'QL-X-138', 'XMD15-27', 'T0901317', 'Selisistat', 'THZ-2-49', 'KIN001-270', 'THZ-2-102-1', 'AICA Ribonucleotide', 'Vinblastine', 'Cisplatin', 'Cytarabine', 'Docetaxel', 'Methotrexate', 'Tretinoin', 'Gefitinib', 'Navitoclax', 'Vorinostat', 'Nilotinib', 'Refametinib', 'CI-1040', 'Temsirolimus', 'Olaparib', 'Veliparib', 'Bosutinib', 'Lenalidomide', 'Axitinib', 'AZD7762', 'GW441756', 'Lestaurtinib', 'Tanespimycin', 'VX-702', 'Motesanib', 'KU-55933', 'Elesclomol', 'Afatinib', 'Vismodegib', 'PLX-4720', 'BX795', 'NU7441', 'SL0101', 'Doramapimod', 'JNK Inhibitor VIII', 'Nutlin-3a (-)', 'PD173074', 'ZM447439', 'RO-3306', 'MK-2206', 'Palbociclib', 'Dactolisib', 'Pictilisib', 'AZD8055', 'PD0325901', 'SB590885', 'Selumetinib', 'CCT007093', 'EHT-1864', 'Cetuximab', 'PF-4708671', 'Serdemetan', 'TW 37', 'CCT-018159', 'Rucaparib', 'SB505124', 'Tamoxifen', 'PFI-1', 'IOX2', 'YK-4-279', '(5Z)-7-Oxozeaenol', 'Piperlongumine', 'Daporinad', 'Talazoparib', 'rTRAIL', 'UNC1215', 'SGC0946', 'ICL1100013', 'XAV939', 'Trametinib', 'Dabrafenib', 'Temozolomide', 'Bleomycin (50 uM)', 'SN-38', 'PFI-3'])

input_value = solara.reactive([solara.reactive(0) for _ in range(len(input_label.value))])
x = "Drug"
output_value = solara.reactive('')
disable_random = solara.reactive(False)
disable = solara.reactive(False)

import joblib
model = joblib.load('models/table_6.joblib')
encoder = joblib.load('models/y_6.joblib')
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

max_value = solara.reactive(12.900156)
min_value = solara.reactive(-9.846829)
close_zero_count = solara.reactive(52)
zero_max_value = solara.reactive(-5)

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
def IC50():
    CellLineButton()
    solara.Text("ln(IC50) (Gaussian Naive Bayes)", style='margin-top:1rem;font-size:1.2rem;')
    solara.Text('Prediction: {}'.format(output_value.value), style='padding-top:1rem')
    with solara.Div(style='text-align: center;display: flex;justify-content: space-between; align-items: center'):
        solara.Button('Random', on_click=fill_random_values, color='indigo', style='color:white; width:7rem', disabled=disable_random.value)
        with solara.Div(style='text-align: center;display: flex;gap: 3rem; align-items: center'):
            solara.InputInt("Close to zero ({} max)".format(len(input_label.value)), value=close_zero_count)
            solara.InputFloat("Close to zero upper limit".format(len(input_label.value)), value=zero_max_value)
            solara.InputFloat("Min", value=min_value)
            solara.InputFloat("Max", value=max_value)
    PredictForm(input_value, input_label, predict_output, x, disable)