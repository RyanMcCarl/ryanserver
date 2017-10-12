#!/usr/bin/env/python

#import flask_pytest
import os
import pytest
import sys
from flask import Flask, render_template, session, redirect, url_for, make_response
from app import create_app

def test_addition():
    with pytest.raises(AssertionError(" error")):
        1 == 2

class Flask(Flask):
    testing = True

@pytest.fixture
def app():
    app = create_app()
    app.testing = True
    return app

@pytest.fixture
def client(app):
    return app.test_client()

# Views
@pytest.fixture
def test_fake_route_raises_exception(client):
    assert client.get(url_for('fakeroute')).status_code == 404

@pytest.fixture
def test_main(client):
   assert client.get(url_for('main')).status_code == 200

@pytest.fixture
def test_todo(client):
   assert client.get(url_for('todo')).status_code == 200

