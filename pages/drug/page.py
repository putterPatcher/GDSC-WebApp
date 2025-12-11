import solara
from components.buttons import HomeButton

list_links = ['FP', 'ExtFP', 'EstateFP', 'GraphFP', 'MACCSFP', 'PubchemFP', 'SubFP', 'KRFP', 'AD2D']
list_button = ['FP', 'ExtFP', 'EstateFP', 'GraphFP', 'MACCSFP', 'PubchemFP', 'SubFP', 'KRFP', 'AD2D']

@solara.component
def Drug():
    HomeButton()
    with solara.Column(gap="10px", align='center'):
        for i in range(len(list_links)):
            with solara.Link(list_links[i]):
                solara.Button(list_button[i], color='red', style='color:white')