from flask import Flask
from .db import db, migrate
from .models import task, goal
from .routes.task_routes import tasks_bp
from .routes.goal_routes import goals_bp
import os

def create_app(config=None):
    app = Flask(__name__)

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('SQLALCHEMY_DATABASE_URI')
    # app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('SLACK_API_TOKEN')

    if config:
        # Merge `config` into the app's configuration
        # to override the app's default settings for testing
        app.config.update(config)

    db.init_app(app)
    migrate.init_app(app, db)

    # Register Blueprints here

    app.register_blueprint(tasks_bp)
    app.register_blueprint(goals_bp)

    return app
