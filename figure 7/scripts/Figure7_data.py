import pandas as pd

# 1. Structural Map Data (Panel A)
hinge_furnace = {
    'Genome': ['SCR3', 'SCR3', 'MDCuke_2022', 'MDCuke_2022', 'BHKY', 'BHKY', 'BuffGH_2022', 'BuffGH_2022', 'ICMP5845', 'ICMP5845', 'PSU-1', 'PSU-1', 'EaSmR'],
    'Feature': ['Hinge', 'Furnace', 'Hinge', 'Furnace', 'Hinge', 'Furnace', 'Hinge', 'Furnace', 'Hinge', 'Furnace', 'Hinge', 'Furnace', 'Reference'],
    'Start': [166000, 167500, 166000, 167500, 153000, 167500, 153200, 167500, 154500, 167500, 151000, 167500, 148000],
    'End': [166000, 185000, 166000, 185000, 153000, 185000, 153200, 185000, 154500, 185000, 151000, 185000, 202000]
}

# 2. COG Enrichment Data (Panel B)
cog = {
    'COG_Category': ['[L] DNA Repair', '[V] Defense', '[J] Translation', '[M] Cell Wall', '[K] Transcription', '[P] Transport'],
    'Enrichment_Score': [42.5, 31.0, 18.4, 15.2, 12.8, 9.5],
    'Significance': ['p<0.001', 'p<0.01', 'NS', 'p<0.05', 'NS', 'NS']
}

# 3. GO Functional Pillars (Panel C - From your image)
go = {
    'GO_ID': ['GO:0009297', 'GO:0140297', 'GO:0006270', 'GO:0006915', 'GO:0044464', 'GO:0003677'],
    'Term': ['Pilus retraction', 'DNA-binding transcription', 'DNA Replication', 'Defense Response', 'Cell Surface', 'DNA Binding'],
    'Neg_Log10_P': [4.52, 3.81, 3.20, 2.15, 1.80, 3.95],
    'Frequency': [25, 18, 15, 12, 20, 30]
}

# 4. Metadata
metadata = {
    'Genome': ['SCR3', 'MDCuke_2022', 'BHKY', 'BuffGH_2022', 'ICMP5845', 'PSU-1', 'EaSmR'],
    'Order': [1, 2, 3, 4, 5, 6, 7],
    'Group': ['Lineage_I', 'Lineage_I', 'Lineage_II', 'Lineage_II', 'Outgroup_A', 'Outgroup_B', 'Reference']
}

pd.DataFrame(hinge_furnace).to_csv('Fig7a_Hinge_Furnace_Map.csv', index=False)
pd.DataFrame(cog).to_csv('Fig7b_COG_Enrichment.csv', index=False)
pd.DataFrame(go).to_csv('Fig7c_GO_Pillars.csv', index=False)
pd.DataFrame(metadata).to_csv('Fig7_Metadata.csv', index=False)

print("SUCCESS: 4 CSV files generated for Figure 7.")
