from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

URL = ''
LOG_IN = {'id' : '', 'pwd' : '1q2w3e4r'}

chromeOptions = Options()
chromeOptions.add_argument('--headless')
driver = webdriver.Chrome(chrome_options=chromeOptions,executable_path = 'C:/Users/cuzai/Desktop/Web_Crawling/pythonStudy/Crawling/webdriver/chrome/chromedriver.exe')


# get to the url
print("getting to the url")
driver.get(URL)
driver.implicitly_wait(10)
print("got to the url")

# close pop-up
driver.find_element_by_css_selector('.hd_pops_close.hd_pops_1').click()
driver.implicitly_wait(10)

# log in
print("logging in")
driver.find_element_by_id('mb_id').send_keys(LOG_IN['id'])
driver.find_element_by_id('mb_password').send_keys(LOG_IN['pwd'])
driver.find_element_by_css_selector('.btn.btn-flat.btn-block').click()
driver.implicitly_wait(10)
print("logged in")

# get to the point
# newUrl = input('input URL')

urls = 'https://avsee03.tv/bbs/board.php?bo_table=javc&wr_id=106040&page=7ㄸhttps://avsee03.tv/bbs/board.php?bo_table=javc&wr_id=106038&page=7ㄸhttps://avsee03.tv/bbs/board.php?bo_table=javc&wr_id=105867&page=8ㄸ	https://avsee03.tv/bbs/board.php?bo_table=javc&wr_id=105777&page=9ㄸhttps://avsee03.tv/bbs/board.php?bo_table=javc&wr_id=105599&page=10ㄸhttps://avsee03.tv/bbs/board.php?bo_table=javc&wr_id=105591&page=11ㄸhttps://avsee03.tv/bbs/board.php?bo_table=javc&wr_id=105587&page=11ㄸhttps://avsee03.tv/bbs/board.php?bo_table=javc&wr_id=105464&page=11ㄸhttps://avsee03.tv/bbs/board.php?bo_table=javc&wr_id=105459&page=12ㄸhttps://avsee03.tv/bbs/board.php?bo_table=javc&wr_id=105451&page=13ㄸhttps://avsee03.tv/bbs/board.php?bo_table=javc&wr_id=105446&page=13ㄸhttps://avsee03.tv/bbs/board.php?bo_table=javc&wr_id=104891&page=15'
urlLi = urls.split('ㄸ')

for newUrl in urlLi :
    driver.get(newUrl)
    driver.implicitly_wait(10)

    # video parse Start
    driver.find_element_by_tag_name('iframe').click()
    driver.switch_to_window(driver.window_handles[0])
    # driver.implicitly_wait(10)
    driver.find_element_by_tag_name('iframe').click()
    # driver.implicitly_wait(10)
    driver.switch_to.frame(driver.find_element_by_tag_name('iframe'))
    driver.find_element_by_css_selector('.jw-icon.jw-icon-inline.jw-button-color.jw-reset.jw-icon-settings.jw-settings-submenu-button').click()
    driver.find_element_by_css_selector('.jw-reset.jw-settings-submenu.jw-settings-submenu-active > button:nth-child(3)').click()


    video = driver.find_element_by_css_selector('.jw-video.jw-reset')
    videoURL = video.get_attribute('src')

    print(videoURL)

driver.quit()
