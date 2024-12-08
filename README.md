
# Web Scraping com MyAnimeList

Este projeto faz parte da disciplina de coleta e tratamento de dados do curso de Análise de Dados e Inteligência Artificial da UFMA. O objetivo é realizar a raspagem de dados, tratamento, normalização e transformação dos dados utilizando Python.

## 🚀 Objetivo do Projeto

O projeto visa:
- Raspar dados públicos do site **MyAnimeList**, com foco no ranking de animes.
- Tratar os dados coletados (valores faltantes, ruídos e outliers).
- Normalizar e transformar os dados para melhor compreensão.
- Garantir que a raspagem respeite os Termos de Uso e o arquivo `robots.txt` do site.

---

## 🔍 Verificação Legal

### Termos de Uso
Os termos do site foram revisados e estão disponíveis [aqui](https://myanimelist.net/about/terms_of_use). Foi identificado que:
- O uso para fins **não comerciais** é permitido.
- Não é permitido coletar informações pessoais de usuários.
- É necessário evitar sobrecarregar os servidores.

### Robots.txt
O arquivo `robots.txt` do MyAnimeList, disponível [aqui](https://myanimelist.net/robots.txt), não bloqueia o acesso às páginas públicas de ranking de animes. Assim, a raspagem para fins acadêmicos está em conformidade.

---

## 📋 Pré-requisitos

Para executar o projeto, você precisa ter:
- Python 3.8 ou superior.
- As bibliotecas `requests`, `beautifulsoup4`, `pandas`, `numpy`, `matplotlib` e `scikit-learn`.

Instale os pacotes necessários com o comando:

```bash
pip install -r requirements.txt
```

---

## 🔧 Execução

### 1. Configuração
Clone este repositório e navegue até a pasta do projeto:

```bash
git clone https://github.com/seu-usuario/web-scraping-myanimelist.git
cd web-scraping-myanimelist
```

### 2. Raspagem de Dados
Execute o script para raspar dados do ranking de animes:

```bash
python scrape.py
```

O script irá:
- Coletar informações públicas do ranking de animes, incluindo título, nota, número de membros e link para mais detalhes.
- Respeitar os limites de requisições com um intervalo de 2 segundos entre cada página.

### 3. Tratamento de Dados
Após a raspagem, o script:
- Preenche valores faltantes (se existirem).
- Remove outliers baseados no IQR (Interquartile Range).
- Corrige inconsistências nos dados.

### 4. Normalização e Transformação
Os dados são:
- **Normalizados** (colunas de notas e número de membros).
- **Transformados** para análises avançadas (aplicação de escala logarítmica nos números de membros).

---

## 📊 Visualização de Dados

Gráficos gerados incluem:
- Distribuição das notas dos animes.
- Relação entre o número de membros (em escala logarítmica) e as notas.

Execute o seguinte comando para visualizar:

```bash
python visualize.py
```

---

## 📦 Estrutura do Projeto

```
web-scraping-myanimelist/
├── data/                  # Dados coletados
├── visuals/               # Gráficos gerados
├── scrape.py              # Script de raspagem
├── process_data.py        # Tratamento e transformação de dados
├── visualize.py           # Visualização de dados
├── requirements.txt       # Dependências do projeto
└── README.md              # Documentação do projeto
```

---

## 📖 Documentação

### Fontes de Dados
Os dados foram coletados da seção pública de rankings do MyAnimeList, acessível [aqui](https://myanimelist.net/topanime.php).

### Métodos de Tratamento
- **Valores faltantes**: preenchidos com a média ou valores padrão.
- **Outliers**: identificados e removidos com base no método IQR.
- **Normalização**: realizada com `MinMaxScaler` da biblioteca `scikit-learn`.
- **Transformação logarítmica**: aplicada ao número de membros para compressão de escalas.

---

## 🛠️ Contribuindo

Contribuições são bem-vindas! Para contribuir:
1. Faça um fork deste repositório.
2. Crie uma branch: `git checkout -b sua-branch`.
3. Envie suas alterações: `git push origin sua-branch`.
4. Abra um pull request.

---

## 📝 Licença

Este projeto é destinado apenas para fins acadêmicos e segue os Termos de Uso do MyAnimeList.

**Importante:** O uso dos dados deve respeitar as políticas de privacidade e direitos autorais do site.
