import tornado.ioloop
import tornado.web
from controller import ResultsHandler, ResultsCSVHandler, ResultadosAgrupadosHandler, MaiorIncidenciaHandler

def make_app():
    app = tornado.web.Application([
        (r"/results", ResultsHandler),
        (r"/results/csv", ResultsCSVHandler),
        ("/resultados_agrupados", ResultadosAgrupadosHandler),
        (r"/maior-incidencia/([^/]+)", MaiorIncidenciaHandler),
    ])

    # app.settings['debug'] = True

    return app

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
