from urllib import parse
import requests
from bs4 import BeautifulSoup

class PriceCrawling :
    def __init__(self, product):
        # search from naver shopping about the product
        quotedProduct = parse.quote_plus(product)
        url = 'https://search.shopping.naver.com/search/all.nhn?query=' + quotedProduct + '&cat_id=&frm=NVSHATC'
        print(url)

    def crawl(self):
        req = requests.get('url')




if __name__ == "__main__" :
    PriceCrawling('샴푸').crawl()