import solara

list_links = ['/MSI', '/LN_IC50', '/cell_line', '/drug']
list_button = ['MSI', 'ln(IC50)', 'Cell Line', 'Drug']

@solara.component
def Home():
    with solara.AppBar():
        solara.Head([solara.Title("Explore GDSC"), ])
    with solara.Column(gap="10px", align='center'):
        for i in range(len(list_links)):
            with solara.Link(list_links[i]):
                solara.Button(list_button[i], color='black', style='color:white')