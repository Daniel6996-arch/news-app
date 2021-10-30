import unittest
from app.models import Movie

class MovieTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the News class
    source,title,author,description,url,poster,publishedAt,content
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_news = News('Forbes','Python Must Be Crazy',,'Phantom''A thrilling new Python Series','/khsjha27hbs','/khsjha27hbs',8.5,129993)


    def test_instance(self):
        self.assertTrue(isinstance(self.new_news,News))