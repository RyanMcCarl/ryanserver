from datetime import datetime
from flask import render_template, session, redirect, url_for, make_response
from . import main

@main.route('/index.html', methods=['GET', 'POST'])
@main.route('/', methods=['GET', 'POST'])
def index():
    return "This is the index function of the main route."


# Illustration of dynamic URL
@main.route('/examples/focus/<task>')
def focus(task):
    return "Today I am focusing on {}".format(task)


# Illustration of setting a cookie
@main.route('/examples/cookie')
def cookie():
    resp = make_response('<h1>This document sets a cookie.')
    resp.set_cookie('maker', 'Ryan')
    return resp