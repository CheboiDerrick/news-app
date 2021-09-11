import urllib.request, json
from .models import Source, Article


def configure_request(app):
    global api_key, sources_url, articles_url
    api_key = app.config["NEWS_API_KEY"]
    sources_url = app.config["SOURCES_API_BASE_URL"]
    articles_url = app.config["ARTICLES_API_BASE_URL"]


def get_sources():
    """
    Function that gets the json response to our url request
    """
    get_sources_url = sources_url.format(api_key)

    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)

        sources_results = None

        if get_sources_response["sources"]:
            sources_results_list = get_sources_response["sources"]
            sources_results = process_sources(sources_results_list)

    return sources_results


def process_sources(sources_list):
    """
    Function  that processes the sources result and transform them to a list of Objects

    Args:
        sources-list: A list of dictionaries that contain source details

    Returns :
        sources-result: A list of source objects
    """
    sources_results = []
    for source_item in sources_list:
        id = source_item.get("id")
        name = source_item.get("name")
        description = source_item.get("description")
        url = source_item.get("url")

        source_object = Source(id, name, description, url)
        sources_results.append(source_object)

    return sources_results


def get_articles(source):
    """
    Function that gets the json response to our url request
    """
    get_articles_url = articles_url.format(source, api_key)
    with urllib.request.urlopen(get_articles_url) as url:
        get_articles_data = url.read()
        get_articles_response = json.loads(get_articles_data)

        articles_results = None

        if get_articles_response["articles"]:
            articles_results_list = get_articles_response["articles"]
            articles_results = process_articles(articles_results_list)

    return articles_results


def process_articles(articles_list):
    """
    Function  that processes the articles result and transform them to a list of Objects

    Args:
        articles_list: A list of dictionaries that contain article details

    Returns :
        articles_results: A list of article objects
    """
    articles_results = []
    for article_item in articles_list:
        author = article_item.get("author")
        title = article_item.get("title")
        description = article_item.get("description")
        url = article_item.get("url")
        urlToImage = article_item.get("urlToImage")
        publishedAt = article_item.get("publishedAt")

        article_object = Article(
            author, title, description, url, urlToImage, publishedAt
        )
        articles_results.append(article_object)

    return articles_results
