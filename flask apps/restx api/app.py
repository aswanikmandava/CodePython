from flask import Flask
from flask_restx import Api, Resource

app = Flask(__name__)
api = Api(app)

@api.route("/hello")
class HelloWorld(Resource):
    def get(self):
        return { "welcome": "hello, world !!!"}

if __name__ == "__main__":
    app.run(debug=True)

