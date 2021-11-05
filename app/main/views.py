from flask import render_template,request,redirect,url_for
from . import main
from ..requests import get_news,get_sources
from ..models import Article,Source

@main.route('/')
def index():
    '''
    View root page function that returns the source page and some data
    '''
  
    # Getting news sources
    #new_source = get_sources('new')
    business_source = get_sources('business')
    entertainment_source = get_sources('entertainment')
    sports_source = get_sources('sports')
    
    title = 'Sources - Welcome to The best News resource Online'
    return render_template('source.html', title = title, business = business_source, entertainment = entertainment_source, sports = sports_source )

@main.route('/articles')
def articles():

    '''
    View root page function that returns the index page and its data
    '''
     # Getting news articles
    tesla_news = get_news('everything','q','tesla')
    apple_news = get_news('everything','q','apple')
    us_news = get_news('top-headlines','country','us')
    techcrunch_news = get_news('everything','sources','techcrunch')
    title = 'Home - Welcome to The best News resource Online'
    return render_template('news.html', title = title, tesla = tesla_news, apple = apple_news, techcrunch = techcrunch_news )
    