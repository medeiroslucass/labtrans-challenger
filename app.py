import tornado.ioloop
import tornado.web
from controller import ResultsHandler, ResultadosAgrupadosHandler, MaiorIncidenciaHandler, \
    VideoHandler, RodoviaHandler
import os

# Obtém o diretório atual do arquivo app.py
current_dir = os.path.dirname(os.path.abspath(__file__))

# Obtém o caminho absoluto para o diretório data dentro do container
data_dir = os.path.join(current_dir, 'data')
def make_app():
    # Obtém o caminho absoluto para o arquivo labtrans.db dentro do diretório data
    db_path = os.path.join(data_dir, 'labtrans.db')
    app = tornado.web.Application([
        (r"/results", ResultsHandler),
        ("/resultados_agrupados", ResultadosAgrupadosHandler),
        (r"/maior-incidencia/([^/]+)", MaiorIncidenciaHandler),
        (r"/videos", VideoHandler),
        (r"/rodovias", RodoviaHandler),
    ])

    app.settings['debug'] = True
    # Configura o caminho do arquivo labtrans.db no objeto Application
    app.settings['db_path'] = db_path
    return app


if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()