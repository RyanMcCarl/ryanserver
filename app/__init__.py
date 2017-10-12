#!/usr/bin/python3
#

import os
import sys
from flask import Flask, render_template
import jinja2
from . import errors
global app
#sys.path.insert(0, os.path.abspath(os.getcwd()))
#sys.path.insert(0, os.path.abspath(os.pardir))

class MyApp(Flask):
    def __init__(self):
        Flask.__init__(self, __name__)
        self.jinja_loader = jinja2.ChoiceLoader([
            self.jinja_loader,
            jinja2.PrefixLoader({}, delimiter = ".")
        ])

    def create_global_jinja_loader(self):
        return self.jinja_loader

    def register_blueprint(self, bp):
        Flask.register_blueprint(self, bp)
        self.jinja_loader.loaders[1].mapping[bp.name] = bp.jinja_loader


def configure_app(app):
    config_name = os.getenv('FLASK_CONFIGURATION') or 'development'
    from .config import config
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    return app

# Define the WSGI application object
def create_app(config_name='development'):
    app = MyApp()
    app = configure_app(app)
    from app.models import db
    db.init_app(app)
    errors.init_app(app)

    # Import a module / component using its blueprint handler variable
    from app.main import main as main_blueprint
    from app.todo import todo as todo_blueprint

    # Register blueprints
    app.register_blueprint(main_blueprint)
    app.register_blueprint(todo_blueprint)
    return app

app = create_app()

# def create_app(config_name='development'):
#     app = Flask(__name__)
#     app = configure_app(app)

#     from app.models import db
#     db.init_app(app)


#     # attach routes and custom error pages here

#     from .main import main# as main_blueprint
#     app.register_blueprint(main)#_blueprint)
#     from .todo import todo#as todo_blueprint
#     app.register_blueprint(todo)#_blueprint)

#     return app

# app = create_app()

# if __name__ == '__main__':
#     create_app()

