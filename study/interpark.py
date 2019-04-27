# 인터파크 투어 사이트에서 여행지 입력 후 검색 → 결과
# 로그인 시 PC웹에서 처리가 어려울 경우 → 모바일 로그인
# 모듈 가져오기

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait # 명시적 대기를 위해서
from selenium.webdriver.support import expected_conditions as EC
import time
from tour import TourInfo
from bs4 import BeautifulSoup

# 사전에 필요한 정보를 로드한다 → DB 혹은 쉘, 배치 파일에서 인자로 받아서 세팅
main_url = 'http://tour.interpark.com/'
keyword = '로마'
# 상품정보를 담는 리스트(TourInfo 리스트)
tour_list = []
# 드라이버 로드
driver = webdriver.Chrome(executable_path='chromedriver.exe')
# 차후 옵션 부여하여(프록시, 에이전트 조작, 이미지를 배제)
# 크롤링을 오래 돌리면 → 임시파일들이 쌓인다. → 직접 템프 파일 삭제 필요

# 사이트 접속(get)
driver.get(main_url)

# 검색창 찾아서 검색어 입력
# id = SearchGNBText
driver.find_element_by_id('SearchGNBText').send_keys(keyword)
#수정할 경우 send_keys 쓸 경우 내용이 붙어버림 →.clear() → send_deys('내용')

# 검색 버튼 클릭
driver.find_element_by_css_selector('.search-btn').click()


# 잠시 대기 → 페이지가 로드되고 나서 즉각적으로 데이터를 획득하는 행위는 자제
# 명시적 대기 → 특정 요소가 locate(발견될때까지) 대기
try :
    element = WebDriverWait(driver, 10).until(
    # 지정한 한 개 요소가 올라오면 웨이트 종료
    EC.presence_of_element_located((By.CLASS_NAME, 'oTravelBox'))
    )
except Exception as e :
    print("Error : ", e)

# 묵시적 대기 → DOM이 다 로드될때까지 대기하고, 언제든 로드되면 바로 진행
#요소를 찾을 특정 시간동안 DOM의 풀림을 지시. 예를 들어 10초 이내라도 발견되면 바로 진행
driver.implicitly_wait(10)
# 절대적 대기 → time.sleep(10) → 클라우드페어(디도스 방어 솔루션)

#더보기 눌러서 게시판 진입
driver.find_element_by_css_selector('.oTravelBox button').click()

# 게시판에서 데이터를 가져올 때 데이터가 많으면 세션(혹시 로그인을 해서 접근되는 사이트일 경우) 관리 필요
# 특정 단위별로 로그인 로그아웃 시도
# 특정 게시물이 사라질 경우 → 팝업 발생(없는...) → 팝업처리 검토 필요
# 게시판 스캔 時 → 임계점을 모른다는 문제(어디가 끝이냐의 문제)
# 게시판 스캔 → 메타정보 획득 → 루프 돌려서 일괄적으로 접근 처리
# searchModule.SetCategoryList(1, '') 스크립트 실행
'''for page in range(1, 27) : # 1~26까지(26은 게시물을 넘어갔을 때 현상을 확인차 넣은 것)
    try :
        # 자바스크립트 구동하기
        driver.execute_script("searchModule.SetCategoryList({}, '')".format(page))
        time.sleep(2)
        print("{} 페이지 이동".format(page))

        # 여러 사이트에서 정보를 수집할 경우 공통정보 정의 단계 필요
        # 상품명, 코멘트, 기간1, 기간2, 가격, 평점, 썸네일, 링크(상품 상세 정보)
    except  Exception as e1 :
        print("오류", e1)'''

try :
    driver.execute_script("searchModule.SetCategoryList(1, '')")
    time.sleep(2)
    boxItems = driver.find_elements_by_css_selector('.oTravelBox li.boxItem')
    # 상품명
    for i in boxItems :
        print("상품명 : ", i.find_element_by_css_selector('.proTit').text)
        print("코멘트 : ", i.find_element_by_css_selector('.proSub').text)
        # 기간
        for a in i.find_elements_by_css_selector('.proInfo') :
            print(a.text)
        print("가격 : ", i.find_element_by_css_selector('.proPrice').text)
        # 이미지를 링크값을 사용할 것인가? 아니면 직접 다운로드해서 우리 서버에 업로드(ftp)할 것인가?
        print("썸네일 : ", i.find_element_by_css_selector('img').get_attribute('src'))
        print("링크 : ", i.find_element_by_css_selector('a').get_attribute('onclick'))
        print("-"*50)
        # 데이터 모음
        obj = TourInfo(
            i.find_element_by_css_selector('.proTit').text,
            i.find_element_by_css_selector('.proPrice').text,
            # 데이터가 부족하거나 없을수도 있으므로 직접 인덱스로 표현은 위험성 있음
            i.find_elements_by_css_selector('.proInfo')[1].text,
            i.find_element_by_css_selector('a').get_attribute('onclick'),
            i.find_element_by_css_selector('img').get_attribute('src')
        )
        tour_list.append(obj)
except Exception as e :
    print("오류", e)

print(tour_list[0].area)


for tour in tour_list :
    # tour = TourInfo
    print(type(tour))
    # 링크데이터에서 실데이터 획득
    arr = tour.link.split(',')
    if arr :
        link = arr[0].replace('searchModule.OnClickDetail(', '')
        # 슬라이싱 : 앞뒤 홑따옴표 제거
        detail_url = link[1:-1]
        # 상세 페이지 이동 : URL 값이 완성된 형태인지 확인 要 (http://)
        driver.get(detail_url)
        time.sleep(2)
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        # 현재 상세정보 페이지에서 스케줄 정보 획득
        data = soup.select('.schedul-all')
        print(type(data))


driver.close()
driver.quit()
import sys
sys.exit()

# 현재 페이지를 Beautiful Soup의 DOM으로 구성
