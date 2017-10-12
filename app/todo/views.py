from datetime import datetime
from flask import current_app, render_template, session, redirect, url_for, make_response
import os
from . import todo
#from app import app, errors, views
from ..models import db


#import app

# Temporary hack until I figure out configuration values
def load_todotxt(todotxt_path='~/Dropbox/todo/todo.txt'):
    with open(os.path.expanduser(todotxt_path)) as infile:
        tasks = sorted([task.strip() for task in infile.readlines()])
    return tasks

@todo.route('/todo/index.html', methods=['GET', 'POST'])
@todo.route('/todo', methods=['GET', 'POST'])
def index():
    return render_template('tasklist.html', tasks=load_todotxt())

