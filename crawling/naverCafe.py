from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time


class NcafeWriteAtt:

    def __init__(self):
        self.driver = webdriver.Chrome('C:/Users/cuzai/Desktop/Web_Crawling/section3/webdriver/chrome/chromedriver')
        self.driver.implicitly_wait(30)

    def Write(self):
        LOG_URL = 'https://nid.naver.com/nidlogin.login?mode=form&url=https%3A%2F%2Fwww.naver.com'

        self.driver.get(LOG_URL)
        self.driver.find_element_by_id('id').send_keys('cuzai')
        self.driver.find_element_by_id('pw').send_keys('tjdghqkr7')
        self.driver.find_element_by_xpath('//*[@id="frmNIDLogin"]/fieldset/input').click()

        self.driver.get('https://cafe.naver.com/AttendanceView.nhn?search.clubid=13764661&search.menuid=278')
        self.driver.switch_to_frame('cafe_main')
        self.driver.find_element_by_id('cmtinput').send_keys('sdfksdfdsfd')

    def __del__(self):
        # self.driver.close()     # 현재 포커스된 영역을 종료
        self.driver.quit()      # 셀레니움 자체를 종료



if __name__ == '__main__' :
    att = NcafeWriteAtt()
    start = time.time()     # 시작시간 체크

    att.Write()
    print(time.time() - start)
