from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from urllib import request,parse
import operator

print('Programme Start...')

# URL = 'https://www.instagram.com/accounts/login/'
chrome_options = Options()
chrome_options.add_argument('--headless')
# driver = webdriver.Chrome(chrome_options = chrome_options, executable_path = 'C:/Users/cuzai/Desktop/Web_Crawling/section3/webdriver/chrome/chromedriver')
driver = webdriver.Chrome('C:/Users/cuzai/Desktop/Web_Crawling/section3/webdriver/chrome/chromedriver')

print('Opening WebDriver...')

keyword = '빅볼청키'
quote = parse.quote_plus(keyword)
getURL = 'https://www.instagram.com/explore/tags/'+quote

driver.get(getURL)
driver.implicitly_wait(10)

print('Webpage Opened...')

# driver.find_element_by_css_selector('body').send_keys(Keys.PAGE_DOWN)
# driver.find_element_by_css_selector('body').send_keys(Keys.PAGE_DOWN)

time.sleep(3)

print('Collecting Contents...')

htags = {}

for i in range(1) :
    rowName = driver.find_elements_by_xpath('//article / div[2] / div / div ')
    for contents in rowName :

        con = contents.find_element_by_xpath('. / div / a').get_attribute('href')

        url = con

        soup = BeautifulSoup(request.urlopen(url), 'html.parser')
        # print(soup.prettify())
        meta = soup.select('meta')
        for t in meta:
            try:
                if t['property'] == 'instapp:hashtags':
                    if t['content'] in htags:
                        htags[t['content']] += 1
                    else:
                        htags[t['content']] = 1
                    print(t['content'])
            except Exception as e:
                if e == KeyError:
                    continue
        time.sleep(1)
        print("-" * 100)


    driver.find_element_by_tag_name('body').send_keys(Keys.PAGE_DOWN)
    time.sleep(1)



sorted_key = sorted(htags.items(), key=operator.itemgetter(1), reverse = True)
print(sorted_key)

#
# print('Collecting Hashtags...')
# soup = BeautifulSoup(driver.page_source, 'html.parser')
#
# popular = soup.select('h2')[0].parent.select_one('div > div > div')
#
# links = []
# for rows in popular :
#     contents = rows.select('div')
#     for con in contents :
#         if con.select_one('a') != None :
#             links.append(con.select_one('a')['href'])
#
# # print(links)
#
# htags = {}
# for i in links :
#     url = 'https://www.instagram.com' + i
#     # print("url")
#     soup = BeautifulSoup(request.urlopen(url), 'html.parser')
#     # print(soup.prettify())
#     meta = soup.select('meta')
#     for t in meta :
#         try :
#             if t['property'] == 'instapp:hashtags' :
#                 if t['content'] in htags :
#                     htags[t['content']] += 1
#                 else :
#                     htags[t['content']] = 1
#         except Exception as e :
#             if e == KeyError :
#                 continue
#
# sorted_key = sorted(htags.items(), key=operator.itemgetter(1), reverse = True)
# print(sorted_key)



time.sleep(10000)

driver.close()