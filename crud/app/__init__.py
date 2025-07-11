from flask import Flask
from config import Config
from app.extensions import db

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Inicializa o banco de dados
    db.init_app(app)

    # Importa e registra blueprints
    from app.blueprints.estoque import bp as estoque_bp
    app.register_blueprint(estoque_bp, url_prefix='/estoque')

    # Importa os modelos para que as tabelas sejam reconhecidas
    from app.blueprints.estoque.models import Produto

    # Cria as tabelas se não existirem
    with app.app_context():
        db.create_all()

    return app
