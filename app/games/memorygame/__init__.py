from flask import Flask, g
from .models import db
from .config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    
    @app.before_request
    def before_request():
        g.db = db
        
    from .memorygame import routes
    app.register_blueprint(memorygame)
    return app
