import requests
import news_collector
import dhvanification
from content import Content

response = requests.get('https://httpbin.org/ip')

print('Your IP is {0}'.format(response.json()['origin']))

content = Content(news_collector.get_news())
dhvanification.dhvanify(content)
