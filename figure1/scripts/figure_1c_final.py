import pandas as pd
import matplotlib.pyplot as plt

# 1. Load the master data
df = pd.read_csv('Panel Feature Category.csv')

# 2. Filter and Pivot for Panel C
panel_c = df[df['Panel'] == 'C'].pivot(index='Feature', columns='Category_Subtype', values='Value')

# 3. Logical Ordering: Sort by Total BGC count (Descending)
panel_c['Total'] = panel_c.sum(axis=1)
panel_c = panel_c.sort_values(by='Total', ascending=False)
panel_c = panel_c.drop(columns=['Total'])

# Ensure columns are in the correct stacking order
panel_c = panel_c[['Conserved', 'Strain-Specific']]

# 4. Setup the Figure
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.sans-serif'] = ['Arial', 'Helvetica', 'DejaVu Sans']
fig, ax = plt.subplots(figsize=(8, 10), facecolor='#FFFFFF')

colors = {'Conserved': '#2ca089', 'Strain-Specific': '#f4c430'}

# 5. Plotting
panel_c.plot(kind='bar', stacked=True, ax=ax, color=colors, width=0.7)

# --- FIX OVERLAP ---
# Place Bold 'C' higher (y=0.98) and adjust plot top margin
fig.text(0.02, 0.98, 'C', fontsize=24, fontweight='bold', ha='left', va='top')
plt.subplots_adjust(top=0.90) # Creates a clear gap between the label and the graph

# 6. Aesthetics & Labels
ax.set_ylabel('Number of Clusters', fontsize=12)
ax.set_xlabel('', fontsize=12)
plt.xticks(rotation=45, ha='right', fontsize=11)
plt.yticks(fontsize=11)

ax.legend(title='BGC Category', labels=['Conserved', 'Strain-Specific'], 
          fontsize=10, title_fontsize=11, frameon=False, loc='upper right')

# Standard Publication "Clean-Up"
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.grid(False)

# 7. Save in high-resolution PNG and PDF
ax.set_facecolor('white')
plt.savefig('Figure_1C_Final_Submission.png', dpi=300, bbox_inches='tight')
plt.savefig('Figure_1C_Final_Submission.pdf', dpi=300, bbox_inches='tight')

print("Success: Figure 1C generated with no overlap and clean aesthetics.")
