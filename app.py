from flask import Flask, render_template
from apps.books.bp import register_welcome_app

APPS_REGISTRY = [register_welcome_app]


def create_app():
    app = Flask(__name__)
    for register_app in APPS_REGISTRY:
        register_app(app)

    @app.route('/')
    def index():
        return render_template('index.html')

    return app


if __name__ == "__main__":
    create_app().run(debug=True)
