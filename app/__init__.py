from flask import Flask
from .db import db, migrate
from .models import customer, rental, video
from .routes.customer_routes import bp as customers_bp
from .routes.video_routes import bp as videos_bp
from .routes.rental_routes import bp as rentals_bp
import os

def create_app(config=None):
    app = Flask(__name__)

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('SQLALCHEMY_DATABASE_URI')

    if config:
        app.config.update(config)

    db.init_app(app)
    migrate.init_app(app, db)

    # Register Blueprints here
    app.register_blueprint(customers_bp)
    app.register_blueprint(videos_bp)
    app.register_blueprint(rentals_bp)

    return app