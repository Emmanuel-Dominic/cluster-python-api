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
    data_status = {
    "result": "OK - healthy"
    }
    rv = client.get('/status')
    assert True
    assert rv.status_code == 200
    assert list(data_status.keys())[0] in rv.data.decode("utf-8")


def test_metrics(client):
    data_metrics = {
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
    assert list(data_metrics.keys())[0] in rv.data.decode("utf-8")
    assert list(data_metrics.keys())[1] in rv.data.decode("utf-8")
    assert list(data_metrics.keys())[2] in rv.data.decode("utf-8")
