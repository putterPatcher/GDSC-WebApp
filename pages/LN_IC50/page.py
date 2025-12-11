import solara
from components.buttons import HomeButton

list_links = ['dataset_1', 'dataset_2']
list_button = ['Dataset 1', 'Dataset 2']

@solara.component
def GDSC():
    HomeButton()
    with solara.Column(gap="10px", align='center'):
        for i in range(len(list_links)):
            with solara.Link(list_links[i]):
                solara.Button(list_button[i])
