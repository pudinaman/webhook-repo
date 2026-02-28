from flask import Flask
from config import Config

from flask_cors import CORS

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    
    # Enable CORS for React development
    CORS(app)

    from app.routes import bp
    app.register_blueprint(bp)

    return app
