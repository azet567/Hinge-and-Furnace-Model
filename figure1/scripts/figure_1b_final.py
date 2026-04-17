import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 1. Load the data
df = pd.read_csv('Panel Feature Category.csv')

# 2. Filter and Pivot for Panel B
panel_b = df[df['Panel'] == 'B'].pivot(index='Feature', columns='Category_Subtype', values='Value')

# 3. Create the figure with extra width to prevent legend overlap
# Using a wider canvas (14 inches) to ensure the legend has its own "lane"
g = sns.clustermap(panel_b, 
                   cmap='YlOrRd', 
                   linewidths=1.2, 
                   linecolor='white',
                   annot=False, 
                   col_cluster=True, 
                   row_cluster=False, 
                   figsize=(14, 10),
                   cbar_pos=None) # We will define the position manually below

# 4. MANUAL LAYOUT REFINEMENT (The "Zero-Overlap" Fix)

# Adjust the main heatmap and dendrogram area to leave room on the right
# left, bottom, width, height
g.gs.update(left=0.1, right=0.80, top=0.90, bottom=0.15)

# Explicitly define a new axis for the legend (cbar) far to the right
# [x_position, y_position, width, height]
cbar_ax = g.fig.add_axes([0.88, 0.35, 0.02, 0.3]) 

# Re-draw the heatmap into the established grid with the external legend axis
sns.heatmap(g.data2d, ax=g.ax_heatmap, cbar_ax=cbar_ax, 
            cmap='YlOrRd', linewidths=1.2, linecolor='white', annot=False,
            cbar_kws={'label': 'Gene Presence', 'ticks': [0, 1]})

# 5. Aesthetics & Labels
g.fig.text(0.05, 0.95, 'B', fontsize=24, fontweight='bold', ha='left', va='top')
cbar_ax.set_yticklabels(['Absence (0)', 'Presence (1)'], fontsize=11)

# Correct alignment for strain labels
plt.setp(g.ax_heatmap.get_xticklabels(), rotation=45, ha='right', rotation_mode='anchor')
g.ax_heatmap.set_xlabel('')
g.ax_heatmap.set_ylabel('')

# 6. Save in both formats
g.savefig('Figure_1B_Final_Submission.pdf', dpi=300, bbox_inches='tight', facecolor='#FFFFFF')
g.savefig('Figure_1B_Final_Submission.png', dpi=300, bbox_inches='tight', facecolor='#FFFFFF')

print("Success: Final Figure 1B generated with isolated legend to prevent overlap.")
