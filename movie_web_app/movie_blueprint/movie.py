from flask import Blueprint, render_template, url_for, session
from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, PasswordField
from wtforms.validators import DataRequired, Length, ValidationError
from password_validator import PasswordValidator
import movie_web_app.adapters.repository as repo
from movie_web_app.authentication.authentication import login_required

movie_blueprint = Blueprint(
    'movie_bp', __name__
)


class SearchForm(FlaskForm):
    movie_title = StringField('Movie title')
    director_name = StringField('Director name')
    actor_name = StringField('Actor name')
    genre_name = StringField('Genre name')
    submit = SubmitField('Find')


class PasswordValid:
    def __init__(self, message=None):
        if not message:
            message = u'Your password must be at least 8 characters, and contain an upper case letter, \
            a lower case letter and a digit'
            self.message = message

        def __call__(self, form, field):
            schema = PasswordValidator()
            schema \
                .min(8) \
                .has().uppercase() \
                .has().lowercase() \
                .has().digits()
            if not schema.validate(field.data):
                raise ValidationError(self.message)


class RegistrationForm(FlaskForm):
    username = StringField('Username', [
        DataRequired(message='Your username is required'),
        Length(min=3, message='Your username is too short')])
    password = PasswordField('Password', [
        DataRequired(message='Your password is required'),
        PasswordValid()])
    submit = SubmitField('Register')


@movie_blueprint.route('/')
def home():
    return render_template(
        'home.html',
        list_movies_url=url_for('movie_bp.list_movies'),
        find_movie_title_url=url_for('movie_bp.find_movie_title'),
        find_movie_director_url=url_for('movie_bp.find_movie_director'),
        find_movie_actor_url=url_for('movie_bp.find_movie_actor'),
        find_movie_genre_url=url_for('movie_bp.find_movie_genre'),
        register_url=url_for('authentication_bp.register'),
        login_url=url_for('authentication_bp.login'),
        logout_url=url_for('authentication_bp.logout'),
        watch_list_url=url_for('movie_bp.watch_list'),
        add_watch_list_url=url_for('movie_bp.add_watch_list'),
    )


@movie_blueprint.route('/list')
def list_movies():
    return render_template(
        'list_movies.html',
        list_movies_url=url_for('movie_bp.list_movies'),
        find_movie_title_url=url_for('movie_bp.find_movie_title'),
        find_movie_director_url=url_for('movie_bp.find_movie_director'),
        find_movie_actor_url=url_for('movie_bp.find_movie_actor'),
        find_movie_genre_url=url_for('movie_bp.find_movie_genre'),
        register_url=url_for('authentication_bp.register'),
        login_url=url_for('authentication_bp.login'),
        logout_url=url_for('authentication_bp.logout'),
        movies=repo.repo_instance
    )


@movie_blueprint.route('/find_movie_title', methods=['GET', 'POST'])
# @login_required
def find_movie_title():
    form = SearchForm()
    if form.validate_on_submit():
        movie = repo.repo_instance.get_movie_title(form.movie_title.data)
        return render_template(
            'list_movies.html',
            list_movies_url=url_for('movie_bp.list_movies'),
            find_movie_title_url=url_for('movie_bp.find_movie_title'),
            find_movie_director_url=url_for('movie_bp.find_movie_director'),
            find_movie_actor_url=url_for('movie_bp.find_movie_actor'),
            find_movie_genre_url=url_for('movie_bp.find_movie_genre'),
            register_url=url_for('authentication_bp.register'),
            login_url=url_for('authentication_bp.login'),
            logout_url=url_for('authentication_bp.logout'),
            movies=movie
        )
    else:
        return render_template(
            'find_movie.html',
            list_movies_url=url_for('movie_bp.list_movies'),
            find_movie_title_url=url_for('movie_bp.find_movie_title'),
            find_movie_director_url=url_for('movie_bp.find_movie_director'),
            find_movie_actor_url=url_for('movie_bp.find_movie_actor'),
            find_movie_genre_url=url_for('movie_bp.find_movie_genre'),
            register_url=url_for('authentication_bp.register'),
            login_url=url_for('authentication_bp.login'),
            logout_url=url_for('authentication_bp.logout'),
            handler_url=url_for('movie_bp.find_movie_title'),
            form=form,
            search_type='movie_title'
        )


@movie_blueprint.route('/find_movie_director', methods=['GET', 'POST'])
# @login_required
def find_movie_director():
    form = SearchForm()
    if form.validate_on_submit():
        movie = repo.repo_instance.get_director_name(form.director_name.data)
        return render_template(
            'list_movies.html',
            list_movies_url=url_for('movie_bp.list_movies'),
            find_movie_title_url=url_for('movie_bp.find_movie_title'),
            find_movie_director_url=url_for('movie_bp.find_movie_director'),
            find_movie_actor_url=url_for('movie_bp.find_movie_actor'),
            find_movie_genre_url=url_for('movie_bp.find_movie_genre'),
            register_url=url_for('authentication_bp.register'),
            login_url=url_for('authentication_bp.login'),
            logout_url=url_for('authentication_bp.logout'),
            movies=movie
        )
    else:
        return render_template(
            'find_movie.html',
            list_movies_url=url_for('movie_bp.list_movies'),
            find_movie_title_url=url_for('movie_bp.find_movie_title'),
            find_movie_director_url=url_for('movie_bp.find_movie_director'),
            find_movie_actor_url=url_for('movie_bp.find_movie_actor'),
            find_movie_genre_url=url_for('movie_bp.find_movie_genre'),
            register_url=url_for('authentication_bp.register'),
            login_url=url_for('authentication_bp.login'),
            logout_url=url_for('authentication_bp.logout'),
            handler_url=url_for('movie_bp.find_movie_director'),
            form=form,
            search_type='director_name'
        )


@movie_blueprint.route('/find_movie_actor', methods=['GET', 'POST'])
# @login_required
def find_movie_actor():
    form = SearchForm()
    if form.validate_on_submit():
        movie = repo.repo_instance.get_actor_name(form.actor_name.data)
        return render_template(
            'list_movies.html',
            list_movies_url=url_for('movie_bp.list_movies'),
            find_movie_title_url=url_for('movie_bp.find_movie_title'),
            find_movie_director_url=url_for('movie_bp.find_movie_director'),
            find_movie_actor_url=url_for('movie_bp.find_movie_actor'),
            find_movie_genre_url=url_for('movie_bp.find_movie_genre'),
            register_url=url_for('authentication_bp.register'),
            login_url=url_for('authentication_bp.login'),
            logout_url=url_for('authentication_bp.logout'),
            movies=movie
        )
    else:
        return render_template(
            'find_movie.html',
            list_movies_url=url_for('movie_bp.list_movies'),
            find_movie_title_url=url_for('movie_bp.find_movie_title'),
            find_movie_director_url=url_for('movie_bp.find_movie_director'),
            find_movie_actor_url=url_for('movie_bp.find_movie_actor'),
            find_movie_genre_url=url_for('movie_bp.find_movie_genre'),
            register_url=url_for('authentication_bp.register'),
            login_url=url_for('authentication_bp.login'),
            logout_url=url_for('authentication_bp.logout'),
            handler_url=url_for('movie_bp.find_movie_actor'),
            form=form,
            search_type='actor_name'
        )


@movie_blueprint.route('/find_movie_genre', methods=['GET', 'POST'])
# @login_required
def find_movie_genre():
    form = SearchForm()
    if form.validate_on_submit():
        movie = repo.repo_instance.get_genre_name(form.genre_name.data)
        return render_template(
            'list_movies.html',
            list_movies_url=url_for('movie_bp.list_movies'),
            find_movie_title_url=url_for('movie_bp.find_movie_title'),
            find_movie_director_url=url_for('movie_bp.find_movie_director'),
            find_movie_actor_url=url_for('movie_bp.find_movie_actor'),
            find_movie_genre_url=url_for('movie_bp.find_movie_genre'),
            register_url=url_for('authentication_bp.register'),
            login_url=url_for('authentication_bp.login'),
            logout_url=url_for('authentication_bp.logout'),
            movies=movie
        )
    else:
        return render_template(
            'find_movie.html',
            list_movies_url=url_for('movie_bp.list_movies'),
            find_movie_title_url=url_for('movie_bp.find_movie_title'),
            find_movie_director_url=url_for('movie_bp.find_movie_director'),
            find_movie_actor_url=url_for('movie_bp.find_movie_actor'),
            find_movie_genre_url=url_for('movie_bp.find_movie_genre'),
            register_url=url_for('authentication_bp.register'),
            login_url=url_for('authentication_bp.login'),
            logout_url=url_for('authentication_bp.logout'),
            handler_url=url_for('movie_bp.find_movie_genre'),
            form=form,
            search_type='genre_name'
        )


@movie_blueprint.route('/watch_list', methods=['GET'])
@login_required
def watch_list():
    return render_template(
        'list_movies.html',
        list_movies_url=url_for('movie_bp.list_movies'),
        find_movie_title_url=url_for('movie_bp.find_movie_title'),
        find_movie_director_url=url_for('movie_bp.find_movie_director'),
        find_movie_actor_url=url_for('movie_bp.find_movie_actor'),
        find_movie_genre_url=url_for('movie_bp.find_movie_genre'),
        register_url=url_for('authentication_bp.register'),
        login_url=url_for('authentication_bp.login'),
        logout_url=url_for('authentication_bp.logout'),
        movies=repo.repo_instance.get_user(session['username']).get_watch_list()
    )


@movie_blueprint.route('/add_watch_list', methods=['GET', 'Post'])
@login_required
def add_watch_list():
    form = SearchForm()
    if form.validate_on_submit():
        movie = repo.repo_instance.get_exact_movie(form.movie_title.data)
        if movie is not None:
            repo.repo_instance.get_user(session['username']).get_watch_list().add_movie(movie)
        return render_template(
            'list_movies.html',
            list_movies_url=url_for('movie_bp.list_movies'),
            find_movie_title_url=url_for('movie_bp.find_movie_title'),
            find_movie_director_url=url_for('movie_bp.find_movie_director'),
            find_movie_actor_url=url_for('movie_bp.find_movie_actor'),
            find_movie_genre_url=url_for('movie_bp.find_movie_genre'),
            register_url=url_for('authentication_bp.register'),
            login_url=url_for('authentication_bp.login'),
            logout_url=url_for('authentication_bp.logout'),
            movies=repo.repo_instance.get_user(session['username']).get_watch_list()
        )
    else:
        return render_template(
            'find_movie.html',
            list_movies_url=url_for('movie_bp.list_movies'),
            find_movie_title_url=url_for('movie_bp.find_movie_title'),
            find_movie_director_url=url_for('movie_bp.find_movie_director'),
            find_movie_actor_url=url_for('movie_bp.find_movie_actor'),
            find_movie_genre_url=url_for('movie_bp.find_movie_genre'),
            register_url=url_for('authentication_bp.register'),
            login_url=url_for('authentication_bp.login'),
            logout_url=url_for('authentication_bp.logout'),
            handler_url=url_for('movie_bp.add_watch_list'),
            form=form,
            search_type='movie_title'
        )
