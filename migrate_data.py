import os
import pandas as pd
from models import Results

# Pasta onde estão os arquivos CSV
pasta_csv = './levantamentos'

# Contador para acompanhar o número de registros inseridos
total_registros = 0

# Percorre todos os arquivos na pasta
for arquivo in os.listdir(pasta_csv):
    if arquivo.endswith('.csv'):
        caminho_arquivo = os.path.join(pasta_csv, arquivo)

        # Leitura do arquivo CSV
        df = pd.read_csv(caminho_arquivo)

        # Inserção dos dados no banco de dados
        for _, linha in df.iterrows():
            resultado = Results(
                name=linha['name'],
                km=linha['km'],
                distance=linha['distance'],
                highway=linha['highway'],
                item=linha['item']
            )
            resultado.save()
            total_registros += 1

            # Exibe o progresso a cada 100 registros inseridos
            if total_registros % 100 == 0:
                print(f"Registros inseridos: {total_registros}")

# Exibe o número total de registros inseridos
print(f"Total de registros inseridos: {total_registros}")
