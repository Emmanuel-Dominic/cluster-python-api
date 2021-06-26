import json
import pytest
from app import app


@pytest.fixture
def client():
    app.config['TESTING'] = True

    with app.app_context():
        with app.test_client() as client:
            yield client

def test_hello(client):
    rv = client.get('/')
    assert True
    assert b'Hello World!' in rv.data
    assert rv.status_code == 200

def test_healthycheck(client):
    data = {
    "result": "OK - healthy"
    }
    rv = client.get('/status')
    assert True
    assert rv.status_code == 200
    assert b'result' in rv.data


def test_metrics(client):
    data = {
    "status": "success",
    "code": 0,
    "data": {
        "UserCount": 140,
        "UserCountActive": 23
        }
    }
    rv = client.get('/metrics')
    assert True
    assert rv.status_code == 200
    assert b'status' in rv.data
    assert b'code' in rv.data
    assert b'data' in rv.data
