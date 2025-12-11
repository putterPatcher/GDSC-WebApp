import solara
from pages.home import Home
from pages.MSI import MSI
from pages.LN_IC50.page import GDSC
from pages.LN_IC50.gdsc_1 import GDSC_1
from pages.LN_IC50.gdsc_2 import GDSC_2
from pages.cell_line.page import CellLine
from pages.cell_line.mutation import Mutation
from pages.cell_line.gene_expression import GeneExpression
from pages.cell_line.dna_methylation import DNAMethylation
from pages.cell_line.copy_number_variation import CopyNumberVariation
from pages.cell_line.AUC import AUC
from pages.cell_line.IC50 import IC50
from pages.drug.page import Drug
from pages.drug.AD2D import AD2D
from pages.drug.EstateFP import EstateFP
from pages.drug.ExtFP import ExtFP
from pages.drug.FP import FP
from pages.drug.GraphFP import GraphFP
from pages.drug.KRFP import KRFP
from pages.drug.MACCSFP import MACCSFP
from pages.drug.PubchemFP import PubchemFP
from pages.drug.SubFP import SubFP

@solara.component
def Page(children):
    solara.AppLayout(navigation=False, children=children)

@solara.component
def PageMSI(children):
    solara.AppLayout(navigation=False, children=children)
    with solara.AppBar():
        with solara.Head():
            solara.Title("Predict MSI")

@solara.component
def PageLN_IC50(children):
    solara.AppLayout(navigation=False, children=children)
    with solara.AppBar():
        with solara.Head():
            solara.Title("Predict ln(IC50)")

@solara.component
def PageCellLine(children):
    solara.AppLayout(navigation=False, children=children)
    with solara.AppBar():
        with solara.Head():
            solara.Title("Predict Cell Line")

@solara.component
def PageDrug(children):
    solara.AppLayout(navigation=False, children=children)
    with solara.AppBar():
        with solara.Head():
            solara.Title("Predict Cell Line")

routes = [
    solara.Route(path='/', component=Home, layout=Page, label="Explore GDSC"),
    solara.Route(path='MSI', component=MSI, layout=PageMSI, label="Micro-Satellite Instability"),
    solara.Route(path='LN_IC50', layout=PageLN_IC50, children=[
        solara.Route(path='/', component=GDSC, label="GDSC"),
        solara.Route(path='dataset_1', component=GDSC_1, label="Dataset 1"),
        solara.Route(path='dataset_2', component=GDSC_2, label="Dataset 2"),
    ]),
    solara.Route(path='cell_line', layout=PageCellLine, children=[
        solara.Route(path='/', component=CellLine, label="Cell Line"),
        solara.Route(path='gene_expression', component=GeneExpression, label="Table 1"),
        solara.Route(path='DNA_Methylation', component=DNAMethylation, label="Table 2"),
        solara.Route(path='mutation', component=Mutation, label="Table 3"),
        solara.Route(path='copy_number_variation', component=CopyNumberVariation, label="Table 4"),
        solara.Route(path='IC50', component=IC50, label='Table 6'),
        solara.Route(path='AUC', component=AUC, label="Table 7")
    ]),
    solara.Route(path='drug', layout=PageDrug, children=[
        solara.Route(path='/', component=Drug, label="Drug"),
        solara.Route(path='AD2D', component=AD2D, label="AD2D"),
        solara.Route(path='EstateFP', component=EstateFP, label="EstateFP"),
        solara.Route(path='ExtFP', component=ExtFP, label="ExtFP"),
        solara.Route(path='FP', component=FP, label="FP"),
        solara.Route(path='GraphFP', component=GraphFP, label="GraphFP"),
        solara.Route(path='KRFP', component=KRFP, label="KRFP"),
        solara.Route(path='MACCSFP', component=MACCSFP, label="MACCSFP"),
        solara.Route(path='PubchemFP', component=PubchemFP, label="PubchemFP"),
        solara.Route(path='SubFP', component=SubFP, label="SubFP"),
    ])
]

