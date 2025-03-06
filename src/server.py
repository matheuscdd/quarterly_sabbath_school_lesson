import json
from lesson import Lesson
from config import Config
from threading import Thread
from werkzeug.exceptions import HTTPException
from flask import Flask, request, jsonify
from models import Body
from pydantic import ValidationError


class Server:
    def __init__(self):
        self.app = Flask(__name__)
        self._register_routes()
        self._register_error_handlers()
        self.app.run(host="0.0.0.0", port=Config.SERVER_PORT, debug=Config.DEBUG)

    def _register_routes(self):
        self.app.add_url_rule("/lesson", "lesson", self.lesson, methods=["POST"])

    def _register_error_handlers(self):
        @self.app.errorhandler(Exception)
        def handle_exception(error):
            if isinstance(error, HTTPException):
                response = {"error": error.name, "message": error.description}
                return jsonify(response), error.code
            return (
                jsonify(
                    {
                        "error": "Internal Server Error",
                        "message": str(error) or "An unexpected error occurred",
                    }
                ),
                500,
            )

    def lesson(self):
        data = request.get_json()
        errors, status_code = self.serializer(data)
        if errors:
            return errors, status_code

        Thread(target=Lesson, args=[data["url"], data["email"]]).start()
        return {"msg": "Track the request in the console"}, status_code

    def serializer(self, data: dict) -> tuple[dict, int]:
        try:
            Body(**data).url_exists(data["url"])
            return [], 202
        except ValidationError as err:
            return jsonify(err.errors()), 400
        except ValueError as err:
            return jsonify(json.loads(str(err))), 404


if __name__ == "__main__":
    Server()
