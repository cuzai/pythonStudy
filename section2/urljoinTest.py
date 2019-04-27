from urllib.parse import urljoin

baseUrl = "http://test.com/html/html2/a.html"
print(">>", urljoin(baseUrl, "b.html"))
print(">>", urljoin(baseUrl, "sub/b.html"))
print(">>", urljoin(baseUrl, "../b.html"))
print(">>", urljoin(baseUrl, "../../b.html"))
