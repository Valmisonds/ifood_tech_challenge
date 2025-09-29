# Case Técnico iFood - Arquitetura de Dados

## Como Executar

### Pré-requisitos

- Python 3.10+
- Git

### 1. Clone o Repositório

```bash
git clone https://github.com/Valmisonds/ifood_tech_challenge.git
cd ifood_tech_challenge
```

### 2. Instale as Dependências

```bash
python -m venv venv
source venv/bin/activate  # use `venv\Scripts\activate`
pip install -r requirements.txt
```

### 3. Baixe os Dados

```bash
mkdir -p data/raw
cd data/raw
wget https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2023-01.parquet
wget https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2023-02.parquet
wget https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2023-03.parquet
wget https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2023-04.parquet
wget https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2023-05.parquet
cd ../..
```

### 4. Processe os Dados

```bash
python src/process_data.py
```

### 5. Execute a Análise

```bash
jupyter lab analysis/ifood_analysis.ipynb


```



