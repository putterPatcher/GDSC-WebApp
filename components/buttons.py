import solara

@solara.component
def HomeButton():
    with solara.Row(justify='end', style='padding:0rem 5rem;'):
        with solara.Link('/'):
            solara.Button('Home', color='success')


@solara.component
def GDSCButton():
    with solara.Row(justify='space-between', style='padding:0rem 5rem;'):
        with solara.Link('/LN_IC50'):
            solara.Button('ln(IC50)', color='primary')
        with solara.Link('/'):
            solara.Button('Home', color='success')

@solara.component
def DrugButton():
    with solara.Row(justify='space-between', style='padding:0rem 5rem;'):
        with solara.Link('/drug'):
            solara.Button('Drug', color='primary')
        with solara.Link('/'):
            solara.Button('Home', color='success')

@solara.component
def CellLineButton():
    with solara.Row(justify='space-between', style='padding:0rem 5rem;'):
        with solara.Link('/cell_line'):
            solara.Button('Cell Line', color='primary')
        with solara.Link('/'):
            solara.Button('Home', color='success')