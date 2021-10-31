from flask import render_template,request,redirect,url_for
from . import main
from ..requests import get_news
from ..models import News

@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
  
    # Getting news articles
    tesla_news = get_news('everything','q','tesla')
    apple_news = get_news('everything','q','apple')
    us_news = get_news('top-headlines','country','us')
    techcrunch_news = get_news('everything','sources','techcrunch')
    title = 'Home - Welcome to The best News resource Online'
    return render_template('news.html', title = title, tesla = tesla_news, apple = apple_news, us = us_news, techcrunch = techcrunch_news )

@main.route('/sources')
def sources():

    '''
    View root page function that returns the index page and some data
    '''

    # Getting news sources
    tesla_news = get_news('tesla')
    apple_news = get_news('apple')
    country = get_news('us')
    sources = get_news('techcrunch')
    title = 'Sources - Welcome to The best News resource Online'
    return render_template('sources.html', title = title, tesla = tesla_news, apple = apple_news, us = country, techcrunch = sources )
