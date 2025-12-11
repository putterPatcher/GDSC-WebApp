import solara
from components.buttons import GDSCButton
import pandas as pd

x_labels = ['TCGA_DESC', 'DRUG_NAME', 'AUC', 'Z_SCORE', 'PATHWAY_NAME', 'PUTATIVE_TARGET']
tcga_desc = ['MB', 'UNCLASSIFIED', 'SKCM', 'BLCA', 'CESC', 'GBM', 'LUAD',
       'LUSC', 'SCLC', 'MESO', 'NB', 'MM', 'PAAD', 'ESCA', 'BRCA', 'HNSC',
       'KIRC', 'LAML', 'OV', 'PRAD', 'COREAD', 'LCML', 'ALL', 'LGG',
       'THCA', 'STAD', 'DLBC', 'UCEC', 'LIHC', 'CLL', 'ACC', 'OTHER']
drug_name = ['Camptothecin', 'Vinblastine', 'Cisplatin', 'Cytarabine',
       'Docetaxel', 'Methotrexate', 'Tretinoin', 'Gefitinib',
       'Navitoclax', 'Vorinostat', 'Nilotinib', 'Refametinib',
       'Temsirolimus', 'Olaparib', 'Veliparib', 'Bosutinib',
       'Lenalidomide', 'Axitinib', 'AZD7762', 'GW441756', 'Lestaurtinib',
       'SB216763', 'Tanespimycin', 'Motesanib', 'KU-55933', 'Elesclomol',
       'Afatinib', 'Vismodegib', 'Staurosporine', 'PLX-4720', 'BX795',
       'NU7441', 'SL0101', 'Doramapimod', 'JNK Inhibitor VIII',
       'Wee1 Inhibitor', 'Nutlin-3a (-)', 'Mirin', 'PD173074', 'ZM447439',
       'Alisertib', 'RO-3306', 'MK-2206', 'Palbociclib', 'Dactolisib',
       'Pictilisib', 'AZD8055', 'PD0325901', 'SB590885', 'Selumetinib',
       'CCT007093', 'Obatoclax Mesylate', 'EHT-1864', 'Avagacestat',
       '5-Fluorouracil', 'Dasatinib', 'Paclitaxel', 'Crizotinib',
       'Rapamycin', 'Sorafenib', 'BI-2536', 'Irinotecan', 'Oxaliplatin',
       'BMS-536924', 'GSK1904529A', 'Tozasertib', 'PF-4708671',
       'PRIMA-1MET', 'Serdemetan', 'TW 37', 'Erlotinib', 'CCT-018159',
       'Rucaparib', 'Niraparib', 'MK-1775', 'Dinaciclib', 'Gemcitabine',
       'Bortezomib', 'GSK269962A', 'SB505124', 'Tamoxifen', 'Fulvestrant',
       'EPZ004777', 'YK-4-279', 'Piperlongumine', 'Daporinad',
       'BMS-345541', 'AZ960', 'Talazoparib', 'XAV939', 'Trametinib',
       'Dabrafenib', 'Temozolomide', 'Bleomycin (50 uM)', 'AZD5438',
       'IAP_5620', 'AZD2014', 'AZD1208', 'AZD1332', 'SN-38',
       'Bicalutamide', 'Ruxolitinib', 'Linsitinib', 'Epirubicin',
       'Cyclophosphamide', 'Pevonedistat', 'Sapitinib', 'Uprosertib',
       'LCL161', 'Lapatinib', 'Luminespib', 'Alpelisib', 'Taselisib',
       'EPZ5676', 'SCH772984', 'IWP-2', 'Leflunomide', 'GSK2801',
       'Bromosporine', 'SGC-CBP30', 'GSK-LSD1', 'BDOCA000347a',
       'BDF00022089a', 'BDILV000379a', 'Entinostat', 'OSI-027', 'LGK974',
       'VE-822', 'WZ4003', 'CZC24832', 'AZD5582', 'GSK2606414', 'PFI3',
       'PCI-34051', 'Wnt-C59', 'I-BET-762', 'RVX-208', 'OTX015', 'GSK343',
       'ML323', 'Entospletinib', 'PRT062607', 'Ribociclib', 'AGI-6780',
       'Picolinici-acid', 'AZD5153', 'CDK9_5576', 'CDK9_5038', 'Eg5_9814',
       'ERK_2440', 'ERK_6604', 'IRAK4_4710', 'JAK1_8709', 'AZD5991',
       'PAK_5339', 'TAF1_5496', 'ULK1_4989', 'VSP34_8731', 'IGF1R_3801',
       'JAK_8517', 'GSK2256098C', 'GSK2276186C', 'GSK2110183B',
       'GSK626616AC', 'GSK3337463A', 'GSK2830371A', 'LMB_AB1', 'LMB_AB2',
       'LMB_AB3', 'AZD4547', 'Ibrutinib', 'Zoledronate', 'Acetalax',
       'Topotecan', 'Teniposide', 'Mitoxantrone', 'Dactinomycin',
       'Bleomycin', 'Fludarabine', 'Nelarabine', 'Dacarbazine',
       'Romidepsin', '123829', '765771', '123138',
       'Podophyllotoxin bromide', '50869', 'Dihydrorotenone', '720427',
       '667880', 'Gallibiscoquinazole', 'L-Oxonoreleagnine', '729189',
       '741909', '743380', 'Elephantin', '150412', 'Sinularin', '615590',
       '630600', 'LMP744', '776928', 'Schweinfurthin A', 'BEN',
       'Sabutoclax', 'LY2109761', 'OF-1', 'MN-64',
       'KRAS (G12C) Inhibitor-12', 'MG-132', 'BDP-00009066', 'Buparlisib',
       'Ulixertinib', 'Venetoclax', 'ABT737', 'Afuresertib', 'AGI-5198',
       'AZD3759', 'AZD5363', 'AZD6738', 'AZD8186', 'Osimertinib',
       'Cediranib', 'Ipatasertib', 'GDC0810', 'GNE-317', 'GSK2578215A',
       'I-BRD9', 'Telomerase Inhibitor IX', 'MIRA-1', 'NVP-ADW742',
       'P22077', 'Savolitinib', 'UMI-77', 'WIKI4', 'Sepantronium bromide',
       'MIM1', 'WEHI-539', 'BPD-00008900', 'N25720-51-A1', 'N27922-53-1',
       'N30652-18-1', 'N29087-69-1', 'HKMTI-1-005', 'ICL-SIRT078',
       'UNC0638', 'AGK2', 'Foretinib', 'BIBR-1532', 'Pyridostatin',
       'AMG-319', 'MK-8776', 'Vinorelbine', 'Mycophenolic acid',
       'Remodelin', 'VX-11e', 'LJI308', 'AZ6102', 'GSK591', 'VE821',
       'VTP-A', 'VTP-B', 'PBD-288', 'POMHEX', 'CT7033-2',
       'GSK-LSD1-2HCl ', '5-azacytidine', 'A-366', 'CPI-637', 'UNC0379',
       'AZD6482', 'AT13148', 'BMS-754807', 'JQ1', 'PFI-1', 'IOX2',
       'CHIR-99021', 'SGC0946', 'GSK2830371', 'THR-101', 'THR-102',
       'THR-103', 'ascorbate (vitamin C)', 'glutathione',
       'alpha-lipoic acid', 'N-acetyl cysteine']
pathway_name = ['DNA replication', 'Mitosis', 'Other', 'EGFR signaling',
       'Apoptosis regulation', 'Chromatin histone acetylation',
       'ABL signaling', 'ERK MAPK signaling', 'PI3K/MTOR signaling',
       'Genome integrity', 'Other, kinases',
       'Protein stability and degradation', 'RTK signaling', 'Cell cycle',
       'WNT signaling', 'JNK and p38 signaling', 'p53 pathway',
       'Cytoskeleton', 'IGF1R signaling', 'Hormone-related',
       'Chromatin histone methylation', 'Metabolism', 'Chromatin other',
       'Unclassified']
putative_target = ['TOP1', 'Microtubule destabiliser', 'DNA crosslinker',
       'Antimetabolite', 'Microtubule stabiliser', 'Retinoic acid',
       'EGFR', 'BCL2, BCL-XL, BCL-W',
       'HDAC inhibitor Class I, IIa, IIb, IV', 'ABL', 'MEK1, MEK2',
       'MTOR', 'PARP1, PARP2', 'SRC, ABL, TEC', 'CRBN',
       'PDGFR, KIT, VEGFR', 'CHEK1, CHEK2', 'NTRK1',
       'FLT3, JAK2, NTRK1, NTRK2, NTRK3', 'GSK3A, GSK3B', 'HSP90',
       'VEGFR, RET, KIT, PDGFR', 'ATM', 'EGFR, ERBB2', 'SMO',
       'Broad spectrum kinase inhibitor', 'BRAF',
       'TBK1, PDK1 (PDPK1), IKK, AURKB, AURKC', 'DNAPK',
       'RSK, AURKB, PIM1, PIM3', 'p38, JNK2', 'JNK', 'WEE1, CHEK1',
       'MDM2', 'MRE11', 'FGFR1, FGFR2, FGFR3', 'AURKA, AURKB', 'AURKA',
       'CDK1', 'AKT1, AKT2', 'CDK4, CDK6',
       'PI3K (class 1), MTORC1, MTORC2', 'PI3K (class 1)',
       'MTORC1, MTORC2', 'PPM1D', 'BCL2, BCL-XL, BCL-W, MCL1',
       'RAC1, RAC2, RAC3', 'Amyloid beta20, Amyloid beta40',
       'Antimetabolite (DNA & RNA)', 'ABL, SRC, Ephrins, PDGFR, KIT',
       'MET, ALK, ROS1', 'MTORC1', 'PDGFR, KIT, VEGFR, RAF',
       'PLK1, PLK2, PLK3', 'DNA alkylating agent', 'IGF1R, IR',
       'AURKA, AURKB, AURKC, others', 'S6K1', 'TP53 activation',
       'BCL2, BCL-XL, MCL1', 'WEE1, PLK1', 'CDK1, CDK2, CDK5, CDK9',
       'Pyrimidine antimetabolite', 'Proteasome', 'ROCK1, ROCK2',
       'TGFBR1, ACVR1B, ACVR1C', 'ESR1', 'ESR', 'DOT1L', 'RNA helicase A',
       'Induces reactive oxygen species', 'NAMPT', 'IKK-1, IKK-2',
       'JAK2, JAK3', 'TNKS1, TNKS2', 'dsDNA break induction', 'CDK2',
       'IAP', 'mTORC1, mTORC2', 'PIM1, PIM2, PIM3', 'NTRK1, NTRK2, NTRK3',
       'AR', 'JAK1, JAK2', 'IGF1R', 'Anthracycline', 'Alkylating agent',
       'NAE', 'EGFR, ERBB2, ERBB3', 'AKT1, AKT2, AKT3',
       'XIAP, IAP1, IAP2', 'PI3Kalpha', 'PI3K (beta sparing)',
       'ERK1, ERK2', 'PORCN', 'Pyrimidine synthesis inhibitor',
       'CECR2, BRD2, BRD4, BRD9', 'EP300, CBP', 'KDM1',
       'BRPF1, BRPF2, BRPF3', 'BAZ2A, BAZ2B', 'HDAC1, HDAC3', 'ATR',
       'NUAK1, NUAK2', 'PI3Kgamma', 'XIAP, cIAP', 'PERK',
       'Polybromo 1, SMARCA4, SMARCA2', 'HDAC8, HDAC6, HDAC1',
       'BRD2, BRD3, BRD4', 'BRD4', 'EZH2', 'USP1, UAF1', 'SYK',
       'IDH2 R140Q mutant', 'Inflammatory related', 'CDK9', 'KSP11',
       'ERK1,ERK2', 'IRAK4', 'JAK1', 'MCL1', 'PAK1, PAK2', 'TAF1', 'ULK1',
       'VSP34', 'IGFR1', 'FAK1', 'JAK1, JAK2, JAK3', 'DYRK1A', 'NIK',
       'ADRA1A, ADRB1', 'GADD34', 'PPP1R15B', 'BTK', ' ', 'TOP2',
       'RNA polymerase', 'CP11A', 'HDAC1, HDAC2, HDAC3, HDAC8',
       'BCL2,  BCL-XL,  BFL1, MCL1', 'TGFB1', 'BRPF1B, BRPF2',
       'KRAS (G12C)', 'Proteasome, CAPN1', 'MRCKB_HUMAN',
       'PI3Kalpha, PI3Kdelta, PI3Kbeta, PI3Kgamma', 'BCL2',
       'BCL2, BCL-XL,  BCL-W, BCL-B, BFL1', 'IDH1 (R132H)',
       'AKT1, AKT2, AKT3, ROCK2', 'PI3Kalpha, PI3Kbeta',
       'VEGFR, FLT1, FLT2, FLT3, FLT4, KIT, PDGFRB', 'AKT1, AKT, AKT3',
       'ESR1, ESR2', 'LRRK2', 'BRD9', 'Telomerase', 'TP53', 'USP7, USP47',
       'MET', 'BIRC5', 'BCL-XL', 'SIR2', 'G9A, GLP',
       'MET, KDR, TIE2, VEGFR3/FLT4, RON, PDGFR, FGFR1, EGFR', 'TERT',
       'G-quadruplex stabiliser', 'CHEK1, CHEK2, CDK2', 'ERK2',
       'RSK2, RSK1, RSK3', 'PMRT5', 'KDM4A, KDM4C, KDM4E, KDM3A, KDM6B',
       'LSD1', 'DNA methyltransferases', 'EHMT1, EHMT2', 'EP300', 'SETD8',
       'PI3Kbeta', 'AKT1', 'BRD2, BRD3, BRD4, BRDT', 'EGLN1', 'WIP1',
       'Mutant RAS', 'anti-oxidant proteins', 'Metabolism']

putative_target_value = solara.reactive('TOP1')
pathway_name_value = solara.reactive('DNA replication')
tcga_desc_value = solara.reactive('MB')
drug_name_value = solara.reactive('Camptothecin')
auc_value = solara.reactive(1)
z_score_value = solara.reactive(1.76)

output_value = solara.reactive('')

import joblib
model = joblib.load('models/gdsc2.joblib')

def predict_output():
    df = pd.DataFrame()
    df[x_labels[0]] = [tcga_desc_value.value, ]
    df[x_labels[1]] = [drug_name_value.value, ]
    df[x_labels[2]] = [auc_value.value, ]
    df[x_labels[3]] = [z_score_value.value, ]
    df[x_labels[4]] = [pathway_name_value.value, ]
    df[x_labels[5]] = [putative_target_value.value, ]
    output_value.value = model.predict(df)[0]

@solara.component
def GDSC_2():
    GDSCButton()
    solara.Text("Dataset 2 (Random Forest Regression)", style='margin-top:1rem;font-size:1.2rem;')
    solara.Text('Prediction: {}'.format(output_value.value), style='padding-top:1rem')
    with solara.Row(justify='center'):
            solara.Button("Predict", on_click=predict_output, style='color:white;background-color:black;width:15rem;')
    solara.Select('TCGA Descriptor', values=tcga_desc, value=tcga_desc_value)
    solara.Select('Drug Name', values=drug_name, value=drug_name_value)
    solara.InputFloat('AUC', value=auc_value, continuous_update=True)
    solara.InputFloat('Z Score', value=z_score_value, continuous_update=True)
    solara.Select('Pathway Name', values=pathway_name, value=pathway_name_value)
    solara.Select('Putative Target', values=putative_target, value=putative_target_value)