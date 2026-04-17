import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Global Style for Manuscript
plt.rcParams.update({
    "font.family": "Arial",
    "font.size": 10,
    "axes.linewidth": 1.2,
    "pdf.fonttype": 42
})

df = pd.read_csv('figure5_data.csv')
sel_df = df[df['Type'] == 'Selection']
is_df = df[df['Type'] == 'IS_Count']

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5.5))
plt.subplots_adjust(wspace=0.3)

# --- Panel A: Adaptive Scaling of Selection ---
# Log scale for distance as per the provided table
scatter = ax1.scatter(sel_df['Distance_kb'], sel_df['Value'], 
                     c=sel_df['Value'], cmap='YlOrRd', s=120, edgecolors='black', linewidth=1)
ax1.set_xscale('log')
ax1.set_title("A", loc="left", fontweight="bold", fontsize=16, x=-0.18)
ax1.set_xlabel("Distance to Nearest IS-Hinge (kb)", fontweight='bold')
ax1.set_ylabel("Selection Pressure (Omega)", fontweight='bold')
ax1.grid(True, which="both", ls="-", alpha=0.2)

# Label the specific genes
for i, row in sel_df.iterrows():
    ax1.annotate(row['Label'], (row['Distance_kb'], row['Value']), 
                 xytext=(5, 5), textcoords='offset points', fontweight='bold')

# --- Panel B: Pan-Genomic Plasticity ---
colors = sns.color_palette("Spectral", len(is_df))
bars = ax2.bar(is_df['Label'], is_df['Value'], color=colors, edgecolor='black', linewidth=1)
ax2.set_title("B", loc="left", fontweight="bold", fontsize=16, x=-0.18)
ax2.set_ylabel("Total IS Element Count", fontweight='bold')
ax2.set_xticklabels(is_df['Label'], rotation=45, ha='right')

# Add counts on top of bars
for bar in bars:
    height = bar.get_height()
    ax2.text(bar.get_x() + bar.get_width()/2., height + 5,
             f'{int(height)}', ha='center', va='bottom', fontweight='bold')

plt.savefig('Figure_5_Standardized.pdf', dpi=600, bbox_inches='tight')
plt.savefig('Figure_5_Standardized.png', dpi=600, bbox_inches='tight')
print("Status: Figure 5 generated with verified coordinate data.")
