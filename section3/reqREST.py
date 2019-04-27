import requests, json

#Rest : POST, GET, PUT(FETCH), DELETE

payload1 = {'key1' : 'value1', 'key2' : 'value2'}   #dict 형태
payload2 = (('key1', 'value1'), ('key2', 'value2')) #tuple 형태
payload3 = {'some' : 'nice'}

#r = requests.put('http://httpbin.org/put', data = payload1)
#print(r.text)

#r= requests.put('https://jsonplaceholder.typicode.com/posts/1', data = payload1)
#print(r.text)

r = requests.delete('https://jsonplaceholder.typicode.com/posts/1')
print(r.text)