import matplotlib.pyplot as plt

def plot_results(p_resist_tempr, resist_compr, taxa_vol_erosao):
    plt.figure(figsize=(7, 8))
    plt.subplot(3, 1, 1)
    plt.hist(p_resist_tempr, bins=100, color='royalblue')
    plt.title('Distribuição da Perda de Resistência Após Altas Temperaturas')

    plt.subplot(3, 1, 2)
    plt.hist(resist_compr, bins=100, color='salmon')
    plt.title('Distribuição da Resistência à Compressão')

    plt.subplot(3, 1, 3)
    plt.hist(taxa_vol_erosao, bins=100, color='lightgreen')
    plt.title('Distribuição da Taxa de Erosão')

    plt.tight_layout()
    plt.show()