import solara
from components.buttons import HomeButton

list_links = ['gene_expression', 'DNA_Methylation', 'mutation', 'copy_number_variation', 'IC50', 'AUC']
list_button = ['Gene Expression', 'DNA Methylation', 'Mutation', 'Copy Number Variation', 'IC50', 'AUC']

@solara.component
def CellLine():
    HomeButton()
    with solara.Column(gap="10px", align='center'):
        for i in range(len(list_links)):
            with solara.Link(list_links[i]):
                solara.Button(list_button[i], color='red', style='color:white')