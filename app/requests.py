import urllib.request,json
from .models import Source

# Getting api key
api_key = None
# Getting the movie base url
sources_url = None

def configure_request(app):
    global api_key,sources_url
    api_key = app.config['NEWS_API_KEY']
    sources_url = app.config['SOURCES_API_BASE_URL']

def get_sources():
    '''
    Function that gets the json response to our url request
    '''
    get_sources_url = sources_url.format(api_key)

    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)

        sources_results = None

        if get_sources_response['sources']:
            sources_results_list = get_sources_response['sources']
            sources_results = process_results(sources_results_list)

    return sources_results

def process_results(sources_list):
    '''
    Function  that processes the movie result and transform them to a list of Objects

    Args:
        movie_list: A list of dictionaries that contain movie details

    Returns :
        movie_results: A list of movie objects
    '''
    sources_results = []
    for source_item in sources_list:
        id = source_item.get('id')
        name = source_item.get('name')
        description = source_item.get('description')
        url = source_item.get('url')

        source_object = Source(id,name,description,url)
        sources_results.append(source_object)

    return sources_results


