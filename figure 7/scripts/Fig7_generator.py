import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from matplotlib.patches import Rectangle

# Set global publication style
plt.rcParams.update({'font.family': 'sans-serif', 'font.sans-serif': ['Arial']})

def draw_plot():
    # Load Data
    try:
        df_map = pd.read_csv('Fig7a_Hinge_Furnace_Map.csv')
        df_cog = pd.read_csv('Fig7b_COG_Enrichment.csv').sort_values('Enrichment_Score', ascending=True)
        df_go = pd.read_csv('Fig7c_GO_Pillars.csv').sort_values('Neg_Log10_P', ascending=True)
        df_meta = pd.read_csv('Fig7_Metadata.csv').sort_values('Order', ascending=False)
    except FileNotFoundError as e:
        print(f"Error: {e}. Make sure the CSV files exist in this folder.")
        return

    fig = plt.figure(figsize=(14, 8), facecolor='white')
    gs = fig.add_gridspec(2, 2, width_ratios=[1.4, 1], hspace=0.3, wspace=0.3)

    # --- PANEL A: COMPARATIVE MAP ---
    ax_a = fig.add_subplot(gs[:, 0])
    genomes = df_meta['Genome'].tolist()
    
    for i, genome in enumerate(genomes):
        y_pos = i + 1
        ax_a.axhline(y_pos, color='#D5D8DC', linewidth=0.8, zorder=0)
        
        g_data = df_map[df_map['Genome'] == genome]
        for _, row in g_data.iterrows():
            if row['Feature'] == 'Furnace':
                ax_a.add_patch(Rectangle((row['Start'], y_pos-0.25), row['End']-row['Start'], 0.5, 
                                         color='#F1948A', alpha=0.7, zorder=1))
            elif row['Feature'] == 'Hinge':
                ax_a.vlines(row['Start'], y_pos-0.4, y_pos+0.4, color='#2E86C1', linewidth=2.5, zorder=2)
            elif row['Feature'] == 'Reference':
                ax_a.add_patch(Rectangle((row['Start'], y_pos-0.1), row['End']-row['Start'], 0.2, 
                                         color='#ABB2B9', zorder=1))

    ax_a.set_yticks(range(1, len(genomes) + 1))
    ax_a.set_yticklabels(genomes, fontweight='bold', fontsize=9)
    ax_a.set_xlabel('Genomic Position (bp)', fontweight='bold', fontsize=10)
    ax_a.set_title('A', loc='left', fontweight='bold', fontsize=18, pad=10)
    ax_a.spines['top'].set_visible(False)
    ax_a.spines['right'].set_visible(False)

    # --- PANEL B: COG ENRICHMENT ---
    ax_b = fig.add_subplot(gs[0, 1])
    # Highlight DNA Repair and Defense in Navy
    colors_b = ['#2C3E50' if 'DNA Repair' in str(cat) or 'Defense' in str(cat) else '#BDC3C7' for cat in df_cog['COG_Category']]
    ax_b.barh(df_cog['COG_Category'], df_cog['Enrichment_Score'], color=colors_b, edgecolor='white')
    ax_b.set_xlabel('Enrichment Score (%)', fontweight='bold', fontsize=9)
    ax_b.set_title('B', loc='left', fontweight='bold', fontsize=18, pad=10)
    ax_b.spines['top'].set_visible(False)
    ax_b.spines['right'].set_visible(False)

    # --- PANEL C: GO BUBBLE PLOT ---
    ax_c = fig.add_subplot(gs[1, 1])
    ax_c.scatter(df_go['Neg_Log10_P'], df_go['Term'], 
                 s=df_go['Frequency']*20, c=df_go['Neg_Log10_P'], 
                 cmap='RdBu_r', edgecolors='#2C3E50', alpha=0.8)
    ax_c.set_xlabel(r'-log$_{10}$(p-value)', fontweight='bold', fontsize=9)
    ax_c.set_title('C', loc='left', fontweight='bold', fontsize=18, pad=10)
    ax_c.spines['top'].set_visible(False)
    ax_c.spines['right'].set_visible(False)

    plt.tight_layout()
    plt.savefig('Fig7_Final.png', dpi=300, bbox_inches='tight')
    plt.savefig('Fig7_Final.pdf', bbox_inches='tight')
    print("DONE: generate_fig7_plot.py has generated Fig7_Final.png and .pdf")

if __name__ == "__main__":
    draw_plot()
