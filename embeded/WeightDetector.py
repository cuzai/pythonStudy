from flask import request
from PriceCrawling import PriceCrawling


class WeightDetector :
    def __init__(self):
        pass

    def detect(self):
        while(True) :
            # get the name of the product
            procuct = request.form('product')
            if procuct :
                PriceCrawling.crawl(procuct)
                break

if __name__ == "__main__" :
    WeightDetector().detect()
