import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 1. CORRECTED DATA (Stopped at n=7 to match your lineages)
data = {
    'Genomes': [1, 2, 3, 4, 5, 6, 7],
    'Pangenome_Mean': [2800, 3420, 3810, 4150, 4420, 4650, 4852],
    'Pangenome_SD': [0, 110, 140, 160, 175, 185, 190],
    'Core_Mean': [2800, 2510, 2400, 2320, 2260, 2200, 2150],
    'Core_SD': [0, 75, 65, 55, 50, 45, 40]
}
df = pd.DataFrame(data)

# 2. Universal Style Header
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.sans-serif'] = ['DejaVu Sans', 'Liberation Sans', 'Arial']
plt.rcParams['pdf.fonttype'] = 42 

fig, ax = plt.subplots(figsize=(8, 6), facecolor='white')

# 3. Plot Pangenome Accumulation (Orange)
ax.errorbar(df['Genomes'], df['Pangenome_Mean'], yerr=df['Pangenome_SD'], 
            fmt='-o', color='#d38441', label='Pangenome (Open, $\gamma=0.16$)', 
            capsize=5, linewidth=2.5, markersize=8, markeredgecolor='white')

# 4. Plot Core Genome Decay (Navy)
ax.errorbar(df['Genomes'], df['Core_Mean'], yerr=df['Core_SD'], 
            fmt='-o', color='#34495e', label='Core Genome', 
            capsize=5, linewidth=2.5, markersize=8, markeredgecolor='white')

# 5. Panel Label and Annotations
# Consistent 'B' position with Panel A
fig.text(0.01, 0.98, 'B', fontsize=26, fontweight='bold', ha='left', va='top')

ax.set_xlabel('Number of Genomes', fontsize=12, fontweight='bold')
ax.set_ylabel('Number of Gene Families', fontsize=12, fontweight='bold')

# Ensure X-axis only shows 1 to 7
ax.set_xticks(range(1, 8))

# Power law annotation
ax.text(3, 5200, r'$f(x) = \kappa \cdot x^{\gamma}$', fontsize=14, color='#d38441')
ax.text(3, 4900, r'$\gamma = 0.16$', fontsize=12, color='#d38441', fontweight='bold')

# 6. Aesthetic Polish
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.legend(frameon=False, loc='center right', fontsize=10)
ax.grid(True, linestyle=':', alpha=0.4)

# Set Y-axis range
ax.set_ylim(1800, 6000)

plt.tight_layout()

# 7. Save
plt.savefig('Figure_2B_Final_Submission.png', dpi=300, bbox_inches='tight')
plt.savefig('Figure_2B_Final_Submission.pdf', dpi=300, bbox_inches='tight')

print("Success: Figure 2B (n=7) generated. Factual error corrected while maintaining style.")
