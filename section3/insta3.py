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

href = []

for i in range(1) :
    rowName = driver.find_elements_by_xpath('//article / div[2] / div / div ')
    for contents in rowName :
        con = contents.find_elements_by_xpath('. / div')
        for c in con :
            link = c.find_element_by_xpath('./a').get_attribute('href')
            if link in href:
                continue
            else :
                href.append(link)

    driver.find_element_by_tag_name('body').send_keys(Keys.PAGE_DOWN)
    time.sleep(1)

print(len(href))

print('Collecting Hashtags...')
htags = {}
for n, i in enumerate(href, 1) :
    try :
        url = i
    except Exception :
        print('error occured')
        continue

    # print("url")
    soup = BeautifulSoup(request.urlopen(url), 'html.parser')
    time.sleep(1)
    # print(soup.prettify())
    meta = soup.select('meta[property]')    #특정 속성값을 찾는 방법
    for t in meta :
        if t['content'] in htags :
            htags[t['content']] += 1
        else :
            htags[t['content']] = 1
        print(t['content'])

    print("-"*100)

sorted_key = sorted(htags.items(), key=operator.itemgetter(1), reverse = True)
print(sorted_key)



# time.sleep(10000)

driver.close()