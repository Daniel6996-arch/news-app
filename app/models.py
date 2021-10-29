class News:
    '''
    News class to define News Objects
    '''

    def __init__(self,source,title,author,description,url,publishedAt,content):
        self.source = source
        self.title = title
        self.author = author
        self.description = description
        self.url = url
        self.urlToImage = urlToImage
        self.publishedAt = publishedAt
        self.content = content