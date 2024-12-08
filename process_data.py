import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import numpy as np

def process_myanimelist_data():
    try:
        df = pd.read_csv("data/myanimelist_ranking.csv")
        print("Dados carregados com sucesso.")
    except FileNotFoundError:
        print("Arquivo não encontrado. Execute o script 'scrape.py' primeiro.")
        return

    print("Verificando valores faltantes...")
    if df.isnull().values.any():
        df.fillna({
            "score": df["score"].mean(),
            "members": 0,
            "episodes": 0,
            "year": 2000
        }, inplace=True)
        
    print("Convertendo colunas para valores numéricos...")
    df["score"] = pd.to_numeric(df["score"], errors="coerce")
    df["members"] = pd.to_numeric(df["members"], errors="coerce")
    df["episodes"] = pd.to_numeric(df["episodes"], errors="coerce")
    df["year"] = pd.to_numeric(df["year"], errors="coerce")
    
    print("Tratando valores inconsistentes...")
    
    # Definir episódios negativos ou NaN como 0
    df["episodes"] = df["episodes"].apply(lambda x: x if x >= 0 else 0)
    
    # Remover anos fora de um intervalo plausível (1950 - ano atual)
    current_year = pd.Timestamp.now().year
    df = df[(df["year"] >= 1970) & (df["year"] <= current_year)]

    print("Removendo outliers com base no IQR para 'members'...")
    Q1 = df["members"].quantile(0.25)
    Q3 = df["members"].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    df = df[(df["members"] >= lower_bound) & (df["members"] <= upper_bound)]

    print("Normalizando os dados de 'members'...")
    scaler = MinMaxScaler()
    df["members_normalized"] = scaler.fit_transform(df[["members"]])

    print("Aplicando transformação logarítmica aos membros...")
    df["members_log"] = np.log1p(df["members"])

    print("Categorizando animes por número de episódios...")
    def categorize_episodes(ep):
        if ep == 1:
            return "1 Episódio"
        elif ep <= 12:
            return "Série curta"
        elif ep <= 24:
            return "Série média"
        elif ep <= 50:
            return "Série longa"
        else:
            return "Série muito longa"

    df["episodes_category"] = df["episodes"].apply(categorize_episodes)

    output_path = "data/myanimelist_processed.csv"
    df.to_csv(output_path, index=False)
    print(f"Dados processados salvos em '{output_path}'.")

if __name__ == "__main__":
    process_myanimelist_data()
