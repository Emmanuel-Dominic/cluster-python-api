from flask import Flask, Response
import logging

app = Flask(__name__)


@app.route("/")
def hello():
    app.logger.info('Main request successfull')
    return "Hello World!"


@app.route("/status")
def healthycheck():
    data = {
    "result": "OK - healthy"
    }
    app.logger.info('Status request successfull')
    return Response(response=data, status=200, mimetype="application/json")


@app.route("/metrics")
def metrics():
    data = {
    "status": "success",
    "code": 0,
    "data": {
        "UserCount": 140,
        "UserCountActive": 23
        }
    }
    app.logger.info('Metrics request successfull')
    return Response(response=data, status=200, mimetype="application/json")


if __name__ == "__main__":
    logging.basicConfig(filename='app.log', level=logging.DEBUG)
    app.run(host='0.0.0.0', port=8080)
