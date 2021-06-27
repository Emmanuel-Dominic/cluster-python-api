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
    assert list(data.keys())[0] == rv.data.decode("utf-8")[0:6]


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
    assert list(data.keys())[0] == rv.data.decode("utf-8")[0:6]
    assert list(data.keys())[1] == rv.data.decode("utf-8")[6:10]
    assert list(data.keys())[2] == rv.data.decode("utf-8")[10:]
