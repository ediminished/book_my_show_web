from flask import Flask, jsonify
from controllers.controller import BookMyShow


def add_routes(app: Flask):
    @app.route("/heartbeat")
    def heart_beat():
        return jsonify(True)

    @app.route("/")
    def welcome():
        res = BookMyShow.get_users()
        return res


def create_app() -> Flask:
    app = Flask(__name__)
    add_routes(app=app)
    return app
