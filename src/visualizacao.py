import matplotlib.pyplot as plt


def plotar_histograma(df):
    plt.hist(df['nota'], bins=10, edgecolor='black')
    plt.title('Distribuição das Notas')
    plt.xlabel('Notas')
    plt.ylabel('Frequência')
    plt.grid(axis='y')

    # Salvar o gráfico como um arquivo
    plt.savefig('distribuicao_notas.png')
    plt.close()  # Fecha a figura para evitar duplicação de gráficos
