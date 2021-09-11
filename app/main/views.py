from flask import render_template, request, redirect, url_for
from . import main
from ..requests import get_sources,get_articles

# Views
@main.route("/")
def index():
    """
    View root page function that returns index page and its data
    """
    # Getting news sources
    sources = get_sources()

    title = "Home - Welcome Quick News"

    return render_template("index.html", title=title, sources=sources)

@main.route("/articles/<id>")
def articles(id):
    articles=get_articles(id)
    print(articles)
    title = f'{id}'

    return render_template('articles.html', title=title, articles=articles)