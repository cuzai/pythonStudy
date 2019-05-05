from selenium import webdriver
from selenium.webdriver.chrome.options import Options

URL = 'https://www.inflearn.com'
LOGIN_INFO = {'id' : 'cuzai',
              'pwd' : 'ha9317je'}

chrome_options = Options()
# chrome_options.add_argument('--headless')

# driver = webdriver.Chrome(chrome_options = chrome_options, executable_path = 'C:/Users/cuzai/Desktop/Web_Crawling/section3/webdriver/chrome/chromedriver')
driver = webdriver.Chrome('C:/Users/cuzai/Desktop/Web_Crawling/section3/webdriver/chrome/chromedriver')
driver.get(URL)
# driver.implicitly_wait(5)
driver.find_element_by_css_selector('ul.topmenu a').click()

driver.find_element_by_name('log').send_keys(LOGIN_INFO['id'])  # 이름으로 태그 찾기
driver.find_element_by_name('pwd').send_keys(LOGIN_INFO['pwd'])
driver.find_element_by_name('user-submit').click()