import pandas as pd
import glob
import os

# Definir caminhos relativos
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
input_dir = os.path.join(base_dir, "data", "raw")
output_dir = os.path.join(base_dir, "data", "processed")

# Criar diretórios se não existirem
os.makedirs(input_dir, exist_ok=True)
os.makedirs(output_dir, exist_ok=True)

# Encontrar todos os arquivos Parquet na pasta de dados brutos
all_files = glob.glob(os.path.join(input_dir, "*.parquet"))

# Ler todos os arquivos Parquet em um único DataFrame
df = pd.concat((pd.read_parquet(f) for f in all_files), ignore_index=True)

# Selecionar e renomear colunas conforme especificado no case
columns_to_keep = {
    "VendorID": "vendor_id",
    "tpep_pickup_datetime": "pickup_datetime",
    "tpep_dropoff_datetime": "dropoff_datetime",
    "passenger_count": "passenger_count",
    "trip_distance": "trip_distance",
    "total_amount": "total_amount",
    "PULocationID": "pickup_location_id",
    "DOLocationID": "dropoff_location_id",
    "payment_type": "payment_type",
    "fare_amount": "fare_amount",
}
df_processed = df[columns_to_keep.keys()].rename(columns=columns_to_keep)

# Converter colunas de datetime
df_processed["pickup_datetime"] = pd.to_datetime(df_processed["pickup_datetime"])
df_processed["dropoff_datetime"] = pd.to_datetime(df_processed["dropoff_datetime"])

# Extrair componentes de data para particionamento
df_processed["year"] = df_processed["pickup_datetime"].dt.year
df_processed["month"] = df_processed["pickup_datetime"].dt.month
df_processed["day"] = df_processed["pickup_datetime"].dt.day
df_processed["hour"] = df_processed["pickup_datetime"].dt.hour

# Salvar o DataFrame processado
output_path = os.path.join(output_dir, "yellow_taxi_processed.parquet")
df_processed.to_parquet(output_path, index=False)

print(f"Dados processados e salvos em {output_path}")
