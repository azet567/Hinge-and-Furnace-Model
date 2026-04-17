import matplotlib.pyplot as plt
import matplotlib.path as mpath
import matplotlib.patches as mpatches
import matplotlib.transforms as mtransforms
import pandas as pd
import numpy as np

# 1. LOAD DATA
df = pd.read_csv('figure_2_flower_data.csv')
core_count = 2150
total_acc = 2702

# 2. SETUP
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.sans-serif'] = ['DejaVu Sans']
fig, ax = plt.subplots(figsize=(10, 10), facecolor='white')
ax.set_xlim(-12, 12)
ax.set_ylim(-12, 12)
ax.axis('off')

# 3. FUNCTION TO DRAW ATTRACTIVE BEZIER PETALS
def draw_petal(ax, angle_deg, color, label, count):
    Path = mpath.Path
    # Elegant tapered shape
    path_data = [
        (Path.MOVETO, [0, 2.8]),
        (Path.CURVE4, [-3.8, 6.8]), 
        (Path.CURVE4, [-2.2, 10.0]),
        (Path.CURVE4, [0, 10.0]),    
        (Path.CURVE4, [2.2, 10.0]),  
        (Path.CURVE4, [3.8, 6.8]),  
        (Path.CURVE4, [0, 2.8]),    
        (Path.CLOSEPOLY, [0, 2.8]),
    ]
    codes, verts = zip(*path_data)
    path = Path(verts, codes)
    
    # Rotation Transform
    t = mtransforms.Affine2D().rotate_deg(angle_deg) + ax.transData
    
    # Attractive Styling: Burnt Orange with a deeper border for pop
    patch = mpatches.PathPatch(path, facecolor=color, alpha=0.85, 
                               ec='#7E5109', lw=2.0, transform=t, zorder=2)
    ax.add_patch(patch)
    
    # Label Positioning
    rad = np.deg2rad(angle_deg + 90)
    tx, ty = 11.2 * np.cos(rad), 11.2 * np.sin(rad)
    ax.text(tx, ty, f"{label}\n({count})", ha='center', va='center', 
            fontweight='bold', fontsize=11, color='#1B2631')

# 4. EXECUTE DRAWING
n_petals = len(df)
angles = np.linspace(0, 360, n_petals, endpoint=False)
for i, (angle, row) in enumerate(zip(angles, df.iloc)):
    draw_petal(ax, -angle, '#E67E22', row['Lineage'], row['Accessory_Count'])

# 5. DRAW CENTER (Core) - Deep Navy
circle = plt.Circle((0, 0), 3.2, color='#1A334E', ec='white', lw=4, zorder=10)
ax.add_patch(circle)
ax.text(0, 0, f"{core_count}\nCore", color='white', 
        ha='center', va='center', fontweight='bold', fontsize=18, zorder=11)

# 6. PERFECTED LABELS
# Increased size to 30 and moved to (0.02, 0.98) for consistent breathing room
fig.text(0.02, 0.98, 'C', fontsize=30, fontweight='bold', ha='left', va='top')

ax.text(0, -11.5, f"Total Accessory Gene Families: {total_acc}", 
        ha='center', fontsize=13, style='italic', fontweight='bold', color='#2C3E50')

plt.tight_layout()
plt.savefig('Figure_2C_Final_Perfect.png', dpi=300, bbox_inches='tight')
plt.savefig('Figure_2C_Final_Perfect.pdf', dpi=300)

print("Success: Figure 2C is now perfected and consistent with Panels A and B.")
