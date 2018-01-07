from html.parser import HTMLParser
import news

class InShortsParser(HTMLParser):

    def __init__(self):
        super(InShortsParser,self).__init__()
        self.articleBody = None
        self.newsItems = []

    def handle_starttag(self, tag, attrs):
        for attr in attrs:
            if(attr[0] == 'itemprop' and attr[1] == 'articleBody'):
                self.articleBody = True

    def handle_data(self, data):
        if bool(self.articleBody):
            self.newsItems.append(news.NewsItem(data))
        self.articleBody = False

    def getNewsArticles(self):
        return self.newsItems