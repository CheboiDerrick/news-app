class Source:
    '''
    Source class to define Source Objects
    '''
    def __init__(self,id,name,description,url):
        self.id =id
        self.name = name
        self.description = description
        self.url = url
    
class  Article:
    '''
    Article class to define Article Objects
    '''
    def __init__(self,author,title,description,url, urlToImage,publishedAt):
        self.author =author
        self.title = title
        self.description = description
        self.url = url
        self.urlToImage=urlToImage
        self.publishedAt=publishedAt