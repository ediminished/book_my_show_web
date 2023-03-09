from flask import Flask, jsonify


def add_routes(app: Flask):
    @app.route("/heartbeat")
    def heart_beat():
        return jsonify(True)

    @app.route("/")
    def welcome():
        return "<h1>Welcome</h1>"


def create_app():
    app = Flask(__name__)
    add_routes(app=app)
    return app
