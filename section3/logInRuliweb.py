import requests
from bs4 import BeautifulSoup

#로그인을 하기 위해서는 기본적으로 id, 비밀번호 그리고 추가로 토큰값까지 요구하는 곳도 있다.
#개발자 도구 network에서 preserve log를 눌러서 로그를 유지시켜준다.
#로그인한다.
#login_proc의 headers에서 내 아이디와 비밀번호 확인 가능. 그리고 거기서 Request URL이 우리가 필요로 하는 정보
# Request Method도 잘 봐라. 이 예제에서는 POST임
#login_result?sid = ... 세션 아이디값을 내려줌. 그리고 이게 쿠키로 저장이 돼서 계속 로그인 유지가 가능한 것

#로그인 유저 정보
LOGIN_INFO = {
    'user_id' : 'tjdghqkr7',
    'user_pw' : 'ha9317je'
}   #대문자로 써 준건 변하지 않는 상수라는 뜻임

#Session 생성, with문 안에서 유지
with requests.Session() as s :
    login_req = s.post('https://user.ruliweb.com/member/login_proc', data = LOGIN_INFO)
    #html 소스 확인
    #print('login_req : ', login_req.text)
    #header 확인
    #print('headr : ', login_req.headers)

    if login_req.status_code == 200 and login_req.ok :  #웹페이지가 잘 열렸으면
        post_one = s.get('https://market.ruliweb.com/read.htm?table=market_ps&page=1&num=4641349&find=&ftext=')
        post_one.raise_for_status() #오류 생기면 말해달라
        soup = BeautifulSoup(post_one.text, 'html.parser')
        #print(soup.prettify())
        article = soup.select('tr .con p')
        for i in article :
            #print("len>>>>>>>", len(i.string))
            if len(i.string) != 1 :
                print(i.string)

