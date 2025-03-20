from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from flask_session import Session

db = SQLAlchemy()
jwt = JWTManager()
migrate = Migrate()  # Create migrate instance
session = Session()  # Create session instance

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)  # Correct way to initialize Flask-Migrate
    jwt.init_app(app)
    session.init_app(app)  # Initialize Flask-Session

    # Register Blueprints
    from app.routes import main_bp
    app.register_blueprint(main_bp)

    return app
