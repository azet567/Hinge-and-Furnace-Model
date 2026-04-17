import matplotlib.pyplot as plt
import pandas as pd

# Typography Sync: Arial
plt.rcParams.update({
    'font.family': 'sans-serif',
    'font.sans-serif': ['Arial'],
    'pdf.fonttype': 42
})

def draw_supp1():
    # Load Data
    df = pd.read_csv('SuppFig1_Null_Dist.csv')
    with open('SuppFig1_Observed.txt', 'r') as f:
        observed = float(f.read())

    plt.figure(figsize=(10, 6), facecolor='white')
    
    # Draw Histogram (Null Distribution)
    n, bins, patches = plt.hist(df['Permutation_Delta_Omega'], bins=40, 
                                color='#AED6F1', edgecolor='#5DADE2', alpha=0.8, 
                                label='Null Distribution (Random)')
    
    # Draw Observed Difference Line
    plt.axvline(observed, color='#CB4335', linestyle='--', linewidth=2.5, 
                label=f'Observed Difference ({observed})')

    # Formatting
    plt.title('Permutation Test: Validation of Genomic Selection Architecture', 
              fontweight='bold', fontsize=14, pad=15)
    plt.xlabel(r'Absolute Difference in Median Omega ($\Delta\omega$)', fontweight='bold')
    plt.ylabel('Frequency', fontweight='bold')
    
    # Clean up spines
    ax = plt.gca()
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.grid(axis='y', linestyle=':', alpha=0.6)
    
    plt.legend(frameon=False)
    
    # Save files
    plt.savefig('Suppl_Fig1_Permutation_Test.png', dpi=300, bbox_inches='tight')
    plt.savefig('Suppl_Fig1_Permutation_Test.pdf', bbox_inches='tight')
    print("DONE: Supplementary Figure 1 generated.")

if __name__ == "__main__":
    draw_supp1()
