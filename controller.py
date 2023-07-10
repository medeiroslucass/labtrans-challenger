import csv
from peewee import fn
from models import Results, Video, Rodovia
import tornado.web
import os
import json


# Função para consultar o Km com maior incidência de um determinado item
def consultar_maior_incidencia(item):
    query = (Results
             .select(Results.km, fn.COUNT(Results.item).alias('incidencia'))
             .where(Results.item == item)
             .group_by(Results.km)
             .order_by(fn.COUNT(Results.item).desc())
             .limit(1))

    resultado = query.get()

    return resultado.km, resultado.incidencia


class ResultsHandler(tornado.web.RequestHandler):

    def get(self):
        query = Results.select(Results.name, Results.km, Results.distance, Results.highway, Results.item)
        results_data = [result.__dict__["__data__"] for result in query]

        self.set_header("Content-Type", "application/json")
        self.write({"results": results_data})




class ResultadosAgrupadosHandler(tornado.web.RequestHandler):
    def get(self):
        # Realizar a consulta na View resultados_agrupados
        query = "SELECT * FROM resultados_agrupados"
        resultados = Results.raw(query)

        # Converter os resultados em um formato adequado (por exemplo, JSON)
        resultados_json = []
        for resultado in resultados:
            resultado_dict = {
                "highway": resultado.highway,
                "km": resultado.km,
                "item": resultado.item,
                "buraco": resultado.buraco,
                "remendo": resultado.remendo,
                "trinca": resultado.trinca,
                "placa": resultado.placa,
                "drenagem": resultado.drenagem
            }
            resultados_json.append(resultado_dict)

        # Retornar os resultados como resposta da API
        self.set_header("Content-Type", "application/json")
        self.write(json.dumps(resultados_json))


# Classe do RequestHandler para o endpoint
class MaiorIncidenciaHandler(tornado.web.RequestHandler):
    def get(self, item):
        km_maior_incidencia, incidencia = consultar_maior_incidencia(item)
        response = {
            'item': item,
            'km_maior_incidencia': km_maior_incidencia,
            'incidencia': incidencia
        }
        self.set_header("Content-Type", "application/json")
        self.write(response)


class VideoHandler(tornado.web.RequestHandler):
    def get(self):
        videos = Video.select()
        videos_data = [video.__dict__["__data__"] for video in videos]
        self.set_header("Content-Type", "application/json")
        self.write({"videos": videos_data})


class RodoviaHandler(tornado.web.RequestHandler):
    def get(self):
        rodovias = Rodovia.select()
        rodovias_data = [rodovia.__dict__["__data__"] for rodovia in rodovias]
        self.set_header("Content-Type", "application/json")
        self.write({"rodovias": rodovias_data})
