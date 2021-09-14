from flask import render_template, request, redirect, url_for
from . import main
from ..requests import get_sources, get_articles, get_articles_from_source

# Views
@main.route("/")
def index():
    """
    View root page function that returns index page and its data
    """
    # Getting news sources
    sources = get_sources()

    # Get news for the carasoul section
    washington = get_articles_from_source("the-washington-post", "1")
    wallstreet = get_articles_from_source("the-wall-street-journal", "1")
    techradar = get_articles_from_source("techradar", "1")
    reuters = get_articles_from_source("reuters", "1")
    espn = get_articles_from_source("espn", "1")

    title = "Home - Welcome Quick News"

    return render_template(
        "index.html",
        title=title,
        sources=sources,
        washington=washington,
        wallstreet=wallstreet,
        techradar=techradar,
        reuters=reuters,
        espn=espn,
    )


@main.route("/articles/<id>")
def articles(id):
    articles = get_articles(id)
    print(articles)
    title = f"{id}"

    return render_template("articles.html", title=title, articles=articles)
