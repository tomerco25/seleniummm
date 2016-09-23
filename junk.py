import json
import urllib2




url='http://api.openweathermap.org/data/2.5/weather?id=294071&appid=b5b39defb5d89dd43c5022d19dec6d0b'

data=urllib2.urlopen(url)
data=json.load(data)
print  data
dd=data['name']
print dd

