class Article:
    '''
    Article class to define News Objects
    '''

    def __init__(self,title,author,description,url,urlToImage,publishedAt,content):
        self.title = title
        self.author = author
        self.description = description
        self.url = url
        self.urlToImage = urlToImage
        self.publishedAt = publishedAt
        self.content = content


class Source:
    '''
    Source class to define source objects
    '''        
    def __init__(self,id,name,description,url,category,country):
        self.id = id
        self.name = name
        self.description =description
        self.url = url
        self.category = category
        self.country = country
