import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

plt.rcParams.update({'font.family': 'sans-serif', 'font.sans-serif': ['Arial']})

def draw_fig8():
    fig = plt.figure(figsize=(16, 10), facecolor='white')
    gs = fig.add_gridspec(2, 4, hspace=0.4, wspace=0.4)

    # Panel A
    ax_a = fig.add_subplot(gs[0, :3])
    df_a = pd.read_csv('Fig8a_Source_Data.csv')
    sns.regplot(data=df_a, x='IS_Count', y='Plasticity_Index', ax=ax_a, 
                scatter_kws={'s':120, 'alpha':0.6, 'color':'#2C3E50'}, 
                line_kws={'color':'#1B2631', 'lw':2.5})
    ax_a.set_title('A', loc='left', fontweight='bold', fontsize=24)
    ax_a.set_ylabel('Plasticity Index (%)', fontweight='bold', fontsize=14)
    ax_a.set_xlabel('Insertion Sequence (IS) Count', fontweight='bold', fontsize=14)

    # Panel B
    ax_b = fig.add_subplot(gs[1, 0])
    df_b = pd.read_csv('Fig8b_Source_Data.csv')
    ax_b.scatter(df_b['Distance_kb'], df_b['Selection_w'], alpha=0.4, s=15, color='#8E44AD')
    ax_b.set_xscale('log'); ax_b.set_yscale('log')
    ax_b.plot(df_b['Distance_kb'], 1.5*(df_b['Distance_kb']**-0.97), color='black', lw=2.5)
    ax_b.set_title('B', loc='left', fontweight='bold', fontsize=24)
    ax_b.set_xlabel('Distance from Hinge (kb)', fontweight='bold', fontsize=12)
    ax_b.set_ylabel(r'Selection Intensity ($\omega$)', fontweight='bold', fontsize=12)

    # Panel C
    ax_c = fig.add_subplot(gs[1, 1])
    df_c = pd.read_csv('Fig8c_Source_Data.csv')
    sns.violinplot(data=df_c, x='Strategy', y='Decay_Constant_Beta', 
                   palette={'Generalist': '#27AE60', 'Specialist': '#F1C40F'}, ax=ax_c, inner="quartile")
    ax_c.set_title('C', loc='left', fontweight='bold', fontsize=24)
    ax_c.set_ylabel(r'Decay Constant ($\beta$)', fontweight='bold', fontsize=12)

    # Panel D
    ax_d = fig.add_subplot(gs[1, 2:])
    df_d = pd.read_csv('Fig8d_Source_Data.csv')
    ax_d.scatter(df_d['ANI'], df_d['TFI'], s=df_d['Size_Mb']*60, alpha=0.6, color='#2980B9', edgecolors='#1B4F72')
    ax_d.axhline(0.5, ls='--', color='#7F8C8D')
    ax_d.set_title('D', loc='left', fontweight='bold', fontsize=24)
    ax_d.set_xlabel('Average Nucleotide Identity (ANI %)', fontweight='bold', fontsize=14)
    ax_d.set_ylabel('Topographic Flux Index (TFI)', fontweight='bold', fontsize=14)

    plt.tight_layout()
    plt.savefig('Fig8_Global_Scaling.png', dpi=300, bbox_inches='tight')
    plt.savefig('Fig8_Global_Scaling.pdf', bbox_inches='tight')
    print("SUCCESS: 10/10 Figure 8 generated.")

if __name__ == "__main__":
    draw_fig8()
