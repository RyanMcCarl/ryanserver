from flask import current_app, Blueprint, render_template
#from ..app import app
#from current_app import db

main = Blueprint('main', __name__, url_prefix='/', template_folder='../templates', static_folder='../static')

from . import views

from app import errors

