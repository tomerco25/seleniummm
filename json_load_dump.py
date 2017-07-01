import json
import urllib2

#dumps object to string
#load string to object:
url='http://api.openweathermap.org/data/2.5/weather?id=294071&appid=b5b39defb5d89dd43c5022d19dec6d0b'

rawdata=urllib2.urlopen(url)

jsondata=urllib2.urlopen(url)
jsondatastring=jsondata.read()
print "--------------RAW json - python convert it to string--------------"
print jsondatastring
print ''

print "1--------------------- json.load - load will convert it to dic&list-------------"
dataload=json.load(rawdata)
print  dataload
print ''

print "3---------------------json.dumps will convert it from dic&list back to string---------"
datadumps=json.dumps(dataload)
print datadumps

print "2---------------------findvalue"
findvalue=dataload['weather'][0]['main']
print findvalue+