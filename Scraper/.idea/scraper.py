'''
This is just to test the ability to scrape a website.

This code was taken from The Hitchhiker's Guide to Python
http://docs.python-guide.org/en/latest/scenarios/scrape/
'''

from lxml import html
import requests

page = requests.get('http://econpy/pythonanywhere.com/ex/001.html')
tree = html.fromstring(page.content)

# create a list of buyers
buyers = tree.xpath('//div[@title="buyer-name"]/text()')
# create a list of prices
prices = tree.xpath('//div[@title="item-price"]/text()')

print( 'Buyers: ', buyers )
print( 'Prices: ', prices )