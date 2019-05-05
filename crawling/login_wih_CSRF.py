import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

URL = 'https://www.wishket.com/accounts/login/'
ua = UserAgent()    # fake user agent 생성. 랜덤으로 useragent를 생성해준다.
# print(ua.ie)
# print(ua.chrome)
# print(ua.random)

with requests.Session() as s :
    s.get(URL)      # CSRF 값을 가져오기 위해 페이지에 한번 방문을 해 줌

    LOGIN_INFO = {
        'identification': 'tjdghqkr7',
        'password': 'ha9317je',
        'csrfmiddlewaretoken' : s.cookies['csrftoken']     #개발자 도구 application 들어가서 csrf 관련 된 값 찾기
    }
    # print(s.cookies['csrftoken']) #토큰값 정상적으로 나옴

    # print(s.headers)    # 헤더값을 한번 알아보자  User-Agent : 우리가 어떤 브라우저(안드로이드, IOS, chrome 등)을 쓰고있는지 확인함

    login_req = s.post(URL, data = LOGIN_INFO, headers = {'User-Agent' : str(ua.chrome), 'Referer' : 'https://www.wishket.com/accounts/login/'})
    # 헤더는 직접 개발자도구에서 보고 붙여넣어줘도 된다.  # Referer는 이 페이지 직전에 내가 어느 페이지에 머물렀는지를 알려주는 것. 마케팅 수단 등으로 이용. 필요시 개발자도구에서 찾아서 넣어줘야 함
    if login_req.status_code == 200 and login_req.ok :
        print(BeautifulSoup(login_req.text, 'html.parser').prettify())