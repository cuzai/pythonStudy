from selenium import webdriver
from selenium.webdriver.chrome.options import Options   #chrome 웹드라이버로 CLI 환경을 사용하기 위함

chromeOptions = Options()
chromeOptions.add_argument('--headless')    #CLI환경으로 구동

# 원래 chrome 웹드라이버는 CLI(Command Line Interface) 환경을 지원하지 않음
driver = webdriver.Chrome(chrome_options = chromeOptions, executable_path = 'C:/Users/cuzai/Desktop/Web_Crawling/section3/webdriver/chrome/chromedriver')

# driver.set_window_size(1920,1280)

driver.get('http://google.com')
driver.save_screenshot('C:/Users/cuzai/Desktop/web1.png')

driver.get('http://www.daum.net')
driver.save_screenshot('C:/Users/cuzai/Desktop/web2.png')

driver.quit()