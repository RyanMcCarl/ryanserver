from datetime import datetime
from flask import render_template, session, redirect, url_for, make_response
from . import todo
import os
from .. import db


#def load_todotxt():
#    with open(app.config['TODOTXT_'] ''~/Dropbox/notes/todo.txt'), mode='r') as infile:
#        tasks = sorted([task.strip() for task in infile.readlines()])
#    return tasks

def load_todotxt():
    with open(app.config['TODOTXT_FILE_PATH']) as infile:
        tasks = sorted([task.strip() for task in infile.readlines()])
    return tasks


@todo.route('/todo/index.html', methods=['GET', 'POST'])
@todo.route('/todo', methods=['GET', 'POST'])
def index():
    return render_template('tasklist.html', tasks=load_todotxt())

