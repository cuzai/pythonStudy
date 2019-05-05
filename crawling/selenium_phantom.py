# 웹 드라이버 다운로드 要

from selenium import webdriver

driver = webdriver.PhantomJS('C:/Users/cuzai/Desktop/Web_Crawling/section3/webdriver/phantomJS/phantomjs')

driver.implicitly_wait(5)   # 암묵적을 5초 쉴 것(리소스가 로딩이 다 되면 그 전에도 움직임)

driver.get('https://google.com')
driver.save_screenshot('C:/Users/cuzai/Desktop/web1.png')   # 스크린샷

driver.implicitly_wait(5)

driver.get('https://www.daum.net')
driver.save_screenshot('C:/Users/cuzai/Desktop/web2.png')   # 스크린샷

driver.quit()