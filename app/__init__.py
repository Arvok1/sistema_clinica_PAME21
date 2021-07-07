from flask import Flask
from app.config import Config
from app.extensions import db, migrate

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    migrate.init_app(app, db)
    return app



#cada arquivo é um módulo
#o __init__.py serve para "inicializar" tudo presente nos arquivos