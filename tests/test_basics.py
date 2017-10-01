#!/usr/bin/env/python

#import flask_pytest
import os
import pytest
import sys

sys.path.insert(0, os.path.abspath(os.getcwd()))
sys.path.insert(0, os.path.abspath(os.pardir))
sys.path.insert(0, os.path.expanduser('~/Dropbox/dev/ryanserver'))

from app import create_app

@pytest.fixture
def app():
    app = create_app()
    app.testing = True
    return app

# Views

@pytest.mark.usefixtures('test_client_class')
class ViewTests:

    def test_main(client):
        assert client.get(url_for('main')).status_code == 200

    def test_todo(client):
        assert client.get(url_for('todo')).status_code == 200


#if __name__ == '__main__':
#    app = app()
#    client = app.test_client()
