from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait # 명시적 대기를 위해서
from selenium.webdriver.support import expected_conditions as EC

chrome_options = Options()
chrome_options.add_argument('--headless')
from selenium.webdriver.chrome.options import Options

# driver = webdriver.Chrome(chrome_options = chrome_options, executable_path = 'C:/Users/cuzai/Desktop/Web_Crawling/section3/webdriver/chrome/chromedriver')
driver = webdriver.Chrome('C:/Users/cuzai/Desktop/Web_Crawling/section3/webdriver/chrome/chromedriver')
URL = 'http://www.encar.com/index.do'

driver.get(URL)
WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, 'manufact')))

driver.find_element_by_id('manufact').click()   # 제조사 클릭
driver.implicitly_wait(5)

manufactsLIst = driver.find_elements_by_css_selector('#manufactListText ul.list_search:nth-of-type(2) li')

for manufact in manufactsLIst :
    if manufact.text == '아우디' :
        manufact.click()
        break
driver.implicitly_wait(5)


seriesList = driver.find_elements_by_css_selector('#seriesItemList li')

for series in seriesList :
    print(series.text)
    if series.text == 'R8' :
        series.click()
        break
driver.implicitly_wait(5)

detail = driver.find_element_by_css_selector('#mdlItemList > li:nth-of-type(2)')
detail.click()

driver.find_element_by_css_selector('.link_search').click()



time.sleep(100)
driver.quit()