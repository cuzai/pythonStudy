import bs4
import urllib.request

url = "https://finance.naver.com/sise/"
req = urllib.request.urlopen(url).read().decode('euc-kr')
soup = bs4.BeautifulSoup(req, 'html.parser')
#print(soup.prettify())

top10 = soup.select('#siselist_tab_0 > tr')

a = 1
for i in top10 :
    if(i.select('a') != []) :
        print("{}. {} : {}".format(a, i.select_one('a').string, i.select_one('td:nth-of-type(5)').string))
        a+=1
