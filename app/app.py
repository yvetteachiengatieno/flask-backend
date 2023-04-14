from flask import Flask, redirect, url_for, render_template, send_file
from . import cookies, simple_pages, orders, api
from app.extensions.databases import db, migrate
from app.cookies.models import Cookie

app = Flask(__name__)
app.config.from_object('app.config')

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config')


    register_extensions(app)
    register_blueprints(app)

    return app

# Blueprints
def register_blueprints(app: Flask):
    #app.register_blueprint(cookies.routes.blueprint)
    app.register_blueprint(simple_pages.routes.blueprint)

def register_extensions(app: Flask):
    db.init_app(app)
    migrate.init_app(app, db, compare_type=True)

    # Blueprints
def register_blueprints(app: Flask):
  app.register_blueprint(cookies.routes.blueprint)
  app.register_blueprint(simple_pages.routes.blueprint)
  app.register_blueprint(orders.routes.blueprint)
  app.register_blueprint(api.routes.blueprint)