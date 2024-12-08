import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

def visualize_myanimelist_data():
    try:
        df = pd.read_csv("data/myanimelist_processed.csv")
        print("Dados carregados com sucesso.")
    except FileNotFoundError:
        print("Arquivo não encontrado. Execute o script 'process_data.py' primeiro.")
        return

    # Gráfico de distribuição de notas
    print("Gerando gráfico de distribuição de notas...")
    plt.figure(figsize=(10, 6))
    plt.hist(df["score"], bins=10, color="blue", edgecolor="black", alpha=0.7)
    plt.title("Distribuição das Notas dos Animes")
    plt.xlabel("Notas")
    plt.ylabel("Frequência")
    plt.savefig("visuals/score_distribution.png")
    print("Gráfico salvo em 'visuals/score_distribution.png'.")
    plt.show()

    # Gráfico de relação entre número de membros (log) e notas
    print("Gerando gráfico de relação entre membros transformados e notas...")
    plt.figure(figsize=(10, 6))
    plt.scatter(df["members_log"], df["score"], alpha=0.6, color="green")
    plt.title("Relação entre Número de Membros (log) e Notas")
    plt.xlabel("Número de Membros (log)")
    plt.ylabel("Notas")
    plt.savefig("visuals/members_vs_score.png")
    print("Gráfico salvo em 'visuals/members_vs_score.png'.")
    plt.show()

    # Gráfico de série temporal: Média de membros ao longo dos anos
    print("Gerando gráfico de séries temporais...")
    plt.figure(figsize=(10, 6))
    time_series = df.groupby("year")["members"].mean()
    ax = time_series.plot(kind="line", marker="o", color="purple")
    plt.title("Média de Membros por Ano de Lançamento")
    plt.xlabel("Ano")
    plt.ylabel("Média de Membros")

    # Ajustando o eixo Y para valores reais com separador de milhar
    formatter = FuncFormatter(lambda x, _: f"{int(x):,}")
    ax.yaxis.set_major_formatter(formatter)

    plt.grid()
    plt.savefig("visuals/members_over_years.png")
    print("Gráfico salvo em 'visuals/members_over_years.png'.")
    plt.show()

    # Gráfico de distribuição de episódios por categoria
    print("Gerando gráfico de distribuição de episódios por categoria...")
    plt.figure(figsize=(10, 6))
    episode_counts = df["episodes_category"].value_counts()
    episode_counts.plot(kind="bar", color="orange", edgecolor="black")
    plt.title("Distribuição de Animes por Categorias de Episódios")
    plt.xlabel("Categoria de Episódios")
    plt.ylabel("Quantidade de Animes")
    plt.xticks(rotation=45)
    plt.savefig("visuals/episode_distribution.png")
    print("Gráfico salvo em 'visuals/episode_distribution.png'.")
    plt.show()

if __name__ == "__main__":
    visualize_myanimelist_data()
