import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1. Load the data
df = pd.read_csv('figure_2_ani_data.csv', index_col=0)

# MODIFICATION: Remove 'MetaG' column and row
if 'MetaG' in df.columns:
    df = df.drop(columns=['MetaG'], index=['MetaG'])

# 2. Setup Figure Aesthetics
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.sans-serif'] = ['DejaVu Sans', 'Liberation Sans', 'Arial']
fig, ax = plt.subplots(figsize=(10, 8), facecolor='white')

# 3. Mask for lower triangle
mask = np.triu(np.ones_like(df, dtype=bool))

# 4. Generate Heatmap
# Using 'RdYlBu_r' for the professional Blue-to-Red transition
sns.heatmap(df, 
            mask=mask, 
            cmap='RdYlBu_r', 
            annot=True, 
            fmt=".2f", 
            square=True, 
            linewidths=1.0, 
            linecolor='white',
            cbar_kws={"shrink": .7, "label": "Nucleotide Identity (%)"})

# 5. MODIFICATION: Move 'A' up and left to avoid overlap
# Previous was (0.02, 0.95). New coordinates: (0.01, 0.98)
fig.text(0.01, 0.98, 'A', fontsize=26, fontweight='bold', ha='left', va='top')

# 6. Final Polish
plt.xticks(rotation=45, ha='right', fontsize=11)
plt.yticks(rotation=0, fontsize=11)
plt.xlabel('')
plt.ylabel('')

plt.tight_layout()

# 7. Save as high-resolution PDF and PNG
plt.savefig('Figure_2A_Final_Submission.png', dpi=300, bbox_inches='tight')
plt.savefig('Figure_2A_Final_Submission.pdf', dpi=300, bbox_inches='tight')

print("Success: Figure 2A (ANI Heatmap) refined. MetaG removed and 'A' position corrected.")
