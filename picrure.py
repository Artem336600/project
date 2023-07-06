import requests

url_cat = 'https://cdn2.thecatapi.com/images/b9r.jpg'
file = open('cat.jpg', 'wb')
file.write(requests.get(url_cat).content)
file.close()














