import requests
url = 'https://jlp.yahooapis.jp/KouseiService/V1/kousei'
response = requests.get(url)

print(response)
# <Response [200]>

print(type(response))
# <class 'requests.models.Response'>