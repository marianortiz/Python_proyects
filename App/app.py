from flask import Flask
from config import config
from routes import Movie

app = Flask(__name__)


def page_not_found(error):
    return "<h3> Page Not Found! </h1>", 404


if __name__ == '__main__':
    app.config.from_object(config['development'])

    # Blueprints
    app.register_blueprint(Movie.main, url_prefix='/api')

    # Errors Handler
    app.register_error_handler(404, page_not_found)
    app.run()
