#!/usr/env/python3
#

from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_mail import Mail
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
from config import config
import sys
import os

sys.path.insert(0, os.path.abspath(os.getcwd()))
sys.path.insert(0, os.path.abspath(os.pardir))
sys.path.insert(0, os.path.expanduser('~/Dropbox/dev/ryanserver'))

bootstrap = Bootstrap()
db = SQLAlchemy()

def create_app(config_name='development'):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    bootstrap.init_app(app)
    db.init_app(app)

    # attach routes and custom error pages here

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    from .todo import todo as todo_blueprint
    app.register_blueprint(todo_blueprint)

    return app


