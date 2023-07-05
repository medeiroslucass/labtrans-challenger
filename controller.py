import csv
from peewee import *
from models import Results


def obter_resultados_agrupados():
    ''' Consulta para agrupar os resultados por km e highway '''
    query = Results.select(Results.highway, Results.km,
                           fn.SUM(Results.item == "Buraco").alias("Buraco"),
                           fn.SUM(Results.item == "Remendo").alias("Remendo"),
                           fn.SUM(Results.item == "Trinca").alias("Trinca"),
                           fn.SUM(Results.item == "Placa").alias("Placa"),
                           fn.SUM(Results.item == "Drenagem").alias("Drenagem")) \
        .group_by(Results.highway, Results.km)

    # Execução da consulta
    resultados = query.dicts()

    # Criação do arquivo CSV
    with open('resultados.csv', 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['highway', 'km', 'buraco', 'remendo', 'trinca', 'placa', 'drenagem'])
        writer.writeheader()
        writer.writerows(resultados)
