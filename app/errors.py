#!/usr/bin/python3

from flask import current_app, Markup, render_template, request
from werkzeug.exceptions import default_exceptions, HTTPException


def error_handler(error):
    msg = "Request resulted in {}".format(error)
    current_app.logger.warning(msg, exc_info=error)

    if isinstance(error, HTTPException):
        description = error.get_description(request.environ)
        code = error.code
        name = error.name
    else:
        description = ("We encountered an error "
                       "while trying to fulfill your request")
        code = 500
        name = 'Internal Server Error'

    # Flask supports looking up multiple templates and rendering the first
    # one it finds.  This will let us create specific error pages
    # for errors where we can provide the user some additional help.
    # (Like a 404, for example).
    templates_to_try = ['errors/{}.html'.format(code), 'errors/generic.html']
    return render_template(templates_to_try,
                           code=code,
                           name=Markup(name),
                           description=Markup(description),
                           error=error)


def init_app(app):
    for exception in default_exceptions:
        app.register_error_handler(exception, error_handler)

    app.register_error_handler(Exception, error_handler)

# This can be used in __init__ with a
# import .errors
# errors.init_app(app)

# #
# from flask import render_template, current_app
# import app
# #from .. import main
# #from .. import todo

# @app.app_errorhandler(404)
# def page_not_found(e):
#     return render_template('404.html'), 404

# @app.app_errorhandler(500)
# def internal_server_error(e):
#     return render_template('500.html'), 500
# # flask_tracking/errors.py
