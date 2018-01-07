import inshorts_parser
import requests

def get_news():
    print("Akash, Welcome!")
    parser = inshorts_parser.InShortsParser()
    response = requests.get('https://www.inshorts.com/en/read')
    parser.feed(response.text)
    return parser.getNewsArticles()