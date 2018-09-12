from flask import Flask
from app import config
from app.api.goods import api_bp
from app.models.bills import db
from flask_bootstrap import Bootstrap

def create_app():
    app = Flask(__name__)
    app.config.from_object(config)
    app.register_blueprint(api_bp, url_prefix='/goods')
    Bootstrap(app=app)
    db.init_app(app)
    # db.drop_all(app=app)
    db.create_all(app=app)
    return app

