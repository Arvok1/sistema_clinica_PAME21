from flask import Flask
from .config import Config
from .extensions import db, migrate
from .consulta.controllers import consulta_api
from .exame.controllers import exame_api
from .medico.controllers import medico_api
from .paciente.controllers import paciente_api
from .receita.controllers import receita_api
from .remedio.controllers import remedio_api

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    app.register_blueprint(consulta_api)
    app.register_blueprint(exame_api)
    app.register_blueprint(medico_api)
    app.register_blueprint(paciente_api)
    app.register_blueprint(receita_api)
    app.register_blueprint(remedio_api)
    db.init_app(app)
    migrate.init_app(app, db)
    return app



#cada arquivo é um módulo
#o __init__.py serve para "inicializar" tudo presente nos arquivos