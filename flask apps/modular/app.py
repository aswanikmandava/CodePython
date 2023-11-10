from app import create_app
from waitress import serve
from config import DevConfig


if __name__ == "__main__":
    app = create_app(config=DevConfig)
    port = app.config.get('APP_SERVER_PORT')
    serve(app, port=port)
    print(f"App started on {port}")
