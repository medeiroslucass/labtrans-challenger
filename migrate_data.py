import os
import pandas as pd
import csv
from models import Results, Video, Rodovia
from peewee import *

# Pasta onde estão os arquivos CSV
pasta_csv_video = './videos'


def create_csv_highway_files():
    highways = Results.select(Results.highway).distinct()

    # Cria a pasta "csv_files" se não existir
    folder_path = "csv_files"
    os.makedirs(folder_path, exist_ok=True)

    for highway in highways:
        query = Results.select(
            Results.highway,
            Results.km,
            fn.SUM(Results.item == "Buraco").alias("buraco"),
            fn.SUM(Results.item == "Remendo").alias("remendo"),
            fn.SUM(Results.item == "Trinca").alias("trinca"),
            fn.SUM(Results.item == "Placa").alias("placa"),
            fn.SUM(Results.item == "Drenagem").alias("drenagem")
        ).where(Results.highway == highway.highway).group_by(Results.highway, Results.km)

        results = query.dicts()

        if results:
            filename = f"resultados_{highway.highway}.csv"
            file_path = os.path.join(folder_path, filename)

            with open(file_path, 'w', newline='') as file:
                fieldnames = ['highway', 'km', 'buraco', 'remendo', 'trinca', 'placa', 'drenagem']
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(results)

    print("CSV files exported successfully.")


# Função para popular a tabela Video
def insert_videos_table():
    for arquivo in os.listdir(pasta_csv_video):
        if arquivo.endswith('.csv'):
            # Extrair o nome do vídeo do caminho do arquivo
            video_nome = os.path.splitext(os.path.basename(arquivo))[0]

            # Abrir o arquivo CSV
            caminho_arquivo = os.path.join(pasta_csv_video, arquivo)
            with open(caminho_arquivo, 'r', newline='') as file:
                reader = csv.DictReader(file)

                # Obter os valores de km_ini e km_final a partir dos dados do arquivo CSV
                km_ini = None
                km_final = None
                for row in reader:
                    if km_ini is None or km_final is None:
                        km_ini = float(row['km'])
                        km_final = float(row['km'])
                    else:
                        km = float(row['km'])
                        if km < km_ini:
                            km_ini = km
                        if km > km_final:
                            km_final = km

                # Criar o registro na tabela Video
                video = Video.create(
                    name=video_nome,
                    km_ini=km_ini,
                    km_final=km_final
                )

                print(f"Registro de vídeo criado: km_ini={km_ini}, km_final={km_final}")


# Função para popular a tabela Rodovia
def insert_rodovia_table():
    pasta_csv_rodovia = "csv_files"  # Pasta onde os arquivos CSV foram criados

    # Percorrer os arquivos CSV na pasta
    for arquivo in os.listdir(pasta_csv_rodovia):
        if arquivo.endswith('.csv'):
            # Obter o número da rodovia do nome do arquivo
            rodovia_numero = int(arquivo.split('_')[1].split('.')[0])
            # Abrir o arquivo CSV
            caminho_arquivo = os.path.join(pasta_csv_rodovia, arquivo)
            with open(caminho_arquivo, 'r', newline='') as file:
                reader = csv.DictReader(file)
                rows = list(reader)

                # Obter os valores de km_ini e km_final a partir dos dados do arquivo CSV
                km_values = [float(row['km']) for row in rows]
                km_ini = min(km_values)
                km_final = max(km_values)

                # Criar o registro na tabela Rodovia
                rodovia = Rodovia.create(
                    highway=rodovia_numero,
                    km_ini=km_ini,
                    km_final=km_final
                )

                print(
                    f"Registro de rodovia criado para a rodovia {rodovia_numero}: km_ini={km_ini}, km_final={km_final}")


def insert_result_table():
    # Contador para acompanhar o número de registros inseridos
    total_registros = 0
    # Percorre todos os arquivos na pasta
    for arquivo in os.listdir(pasta_csv_video):
        if arquivo.endswith('.csv'):
            caminho_arquivo = os.path.join(pasta_csv_video, arquivo)

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

insert_result_table()
# Chamada para criar os csv das rodovias
create_csv_highway_files()
insert_rodovia_table()
# Chamada das funções para popular as tabelas
insert_videos_table()


