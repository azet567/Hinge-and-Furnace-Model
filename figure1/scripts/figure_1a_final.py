import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 1. Load the data
df = pd.read_csv('Panel Feature Category.csv')

# 2. Filter for Panel A and Reshape
panel_a = df[df['Panel'] == 'A'].pivot(index='Feature', columns='Category_Subtype', values='Value')

# REFINEMENT 2: Logical Ordering by Magnitude (Descending by Core values)
# This allows the reader to see the most dominant systems at the top
panel_a = panel_a.sort_values(by='Core', ascending=True)

# 3. Setup the Figure (Sans-serif font standardization)
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.sans-serif'] = ['Arial', 'Helvetica', 'DejaVu Sans']
fig, ax = plt.subplots(figsize=(10, 8), facecolor='#FFFFFF')

# Plotting the horizontal bars
# Colors adjusted to match the deep navy and professional orange from your original
panel_a.plot(kind='barh', ax=ax, color={'Core': '#34495e', 'Accessory': '#d38441'}, width=0.8)

# REFINEMENT 1: Replace Title with Bold 'A' in top-left
# We remove the internal title entirely
ax.set_title('')
fig.text(0.02, 0.95, 'A', fontsize=24, fontweight='bold', ha='left', va='top')

# REFINEMENT 3: Clean Legend and Remove Floating Lines
# Renaming "Category_Subtype" to "Genome Fraction"
ax.legend(title='Genome Fraction', fontsize=11, title_fontsize=12, frameon=False)

# REFINEMENT 4: Font Consistency & Aesthetic Cleaning
ax.set_xlabel('Percentage of Genes (%)', fontsize=12)
ax.set_ylabel('Functional Category', fontsize=12)

# Remove the distracting internal grid lines
ax.grid(False)

# Clean up spines (top and right)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# Ensure Y-axis labels and legend font sizes match
plt.setp(ax.get_yticklabels(), fontsize=11)

plt.tight_layout()

# 5. Save in high-resolution PNG and PDF
ax.set_facecolor('white') # Explicitly setting facecolor to pure white
plt.savefig('Figure_1A_Final_Submission.png', dpi=300, bbox_inches='tight')
plt.savefig('Figure_1A_Final_Submission.pdf', dpi=300, bbox_inches='tight')

print("Success: Figure 1A generated with bold label, logical ordering, and clean aesthetics.")
