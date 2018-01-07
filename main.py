import requests
import news_collector
import dhvanification
import email_sender
from content import Content

response = requests.get('https://httpbin.org/ip')

print('Your IP is {0}'.format(response.json()['origin']))

content = Content(news_collector.get_news())
fileName = dhvanification.dhvanify(content)
# send email
email_sender.send_email(fileName)


