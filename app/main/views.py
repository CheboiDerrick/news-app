from flask import render_template, request, redirect, url_for
from . import main
from ..requests import get_sources

# Views
@main.route("/")
def index():
    """
    View root page function that returns index page and its data
    """
    # Getting popular movie
    sources = get_sources()
    # upcoming_movie = get_movies('upcoming')
    # now_showing_movie = get_movies('now_playing')

    title = "Home - Welcome Quick News"

    return render_template("index.html", title=title, sources=sources)
