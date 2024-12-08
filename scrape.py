import time
import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_myanimelist_ranking():
    base_url = "https://myanimelist.net/topanime.php?limit={}"
    all_data = []

    # loop para acessar as páginas de ranking, pega os 50 primeiros animes de cada página
    for page in range(0, 50, 50): 
        print(f"Scraping page {page // 50 + 1}...")
        url = base_url.format(page)
        response = requests.get(url)

        if response.status_code != 200:
            print(f"Erro ao acessar {url}")
            continue

        soup = BeautifulSoup(response.content, 'html.parser')
        anime_list = soup.find_all('tr', class_='ranking-list')

        for anime in anime_list:
            try:
                rank = anime.find('span', class_='top-anime-rank-text').text.strip()
                title = anime.find('h3', class_='anime_ranking_h3').text.strip().replace(';', '-').replace(',', '-')
                score = anime.find('span', class_='score-label').text.strip()
                info = anime.find('div', class_='information di-ib mt4').text.strip()
                
                # Extraindo membros, episódios e ano
                members = int(info.split('members')[0].split()[-1].replace(',', ''))
                
                episodes = info.split('(')[1].split('eps')[0].strip() if '(' in info else "Unknown"
                year = info.split('-')[0].strip().split()[-1] if '-' in info else "Unknown"

                link = anime.find('a', class_='hoverinfo_trigger')['href']

                all_data.append({
                    "rank": int(rank),
                    "title": title,
                    "score": float(score),
                    "members": members,
                    "episodes": episodes if episodes.isdigit() else "Unknown",
                    "year": int(year) if year.isdigit() else "Unknown",
                    "link": link
                })
            except Exception as e:
                print(f"Erro ao processar um item: {e}")

        time.sleep(2)
        
    if not all_data:
        print("Nenhum dado foi coletado.")
        return

    # Criando dataframe
    df = pd.DataFrame(all_data)
    # Salvando os dados em CSV
    df.to_csv("data/myanimelist_ranking.csv", index=False)
    print("Raspagem concluída. Dados salvos em 'data/myanimelist_ranking.csv'.")

if __name__ == "__main__":
    scrape_myanimelist_ranking()
