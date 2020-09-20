from flask import Flask, request, url_for

import movie_web_app.adapters.repository as repo
from movie_web_app.domain.model import Person
from movie_web_app.adapters.movieFileCSVReader import MovieFileCSVReader


def create_app():
    app = Flask(__name__)
    
    app.config.from_object('config.Config')
    
    repo.repo_instance = MovieFileCSVReader("movie_web_app/adapters/Data1000Movies.csv")

    with app.app_context():
        from .movie_blueprint import movie
        app.register_blueprint(movie.movie_blueprint)
        from .authentication import authentication
        app.register_blueprint(authentication.authentication_blueprint)
    return app
