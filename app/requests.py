import urllib.request,json
from .models import Article, Source


# Getting api key
api_key = None
# Getting the base and sources url
base_url = None
sources_url = None

def configure_request(app):
    global api_key,base_url,sources_url
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config['NEWS_API_BASE_URL']
    sources_url = app.config['NEWS_API_SOURCES_URL']


def get_news(article,q,e):
    '''
    Function that gets the json response to our url request
    '''
    get_news_url = base_url.format(article,q,e,api_key)

    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

        news_results = None  #replacable with []

        if get_news_response['articles']:
            news_results_list = get_news_response['articles']
            news_results = process_articles(news_results_list)


    return news_results


def get_sources(category):
    '''
    Function that gets the json response to our url request
    '''
    get_sources_url = sources_url.format(category,api_key)

    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)

        sources_results = None  #replacable with []

        if get_sources_response['sources']:
            sources_results_list = get_sources_response['sources']
            sources_results = process_sources(sources_results_list)


    return sources_results


def process_articles(news_list): #articles_url
    '''
    Function  that processes the news result and transform them to a list of Objects

    Args:
        news_list: A list of dictionaries that contain news details

    Returns :
        news_results: A list of news objects
    '''
   
    news_results = [] 
    for news_item in news_list:
       
        title = news_item.get('title')
        author = news_item.get('author')
        description = news_item.get('description')
        url = news_item.get('url')
        poster = news_item.get('urlToImage')
        publishedAt = news_item.get('publishedAt')
        content = news_item.get('content')

        if poster:
            news_object = Article(title,author,description,url,poster,publishedAt,content)
            news_results.append(news_object)

    return news_results

def process_sources(sources_list): #sources_url
    '''
    Function  that processes the news result and transform them to a list of Objects

    Args:
        news_list: A list of dictionaries that contain sources details

    Returns :
        news_results: A list of sorces objects
    '''
   
    sources_results = []
    for source_item in sources_list:
       
        id = source_item.get('id')
        name = source_item.get('name')
        description = source_item.get('description')
        url = source_item.get('url')
        category = source_item.get('category')
        country = source_item.get('country')
        source_object = Source(id,name,description,url,category,country)
        sources_results.append(source_object)

    return sources_results


