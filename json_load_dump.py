import json
import urllib2

#dumps object to string
#load string to object:
url='http://api.openweathermap.org/data/2.5/weather?id=294071&appid=b5b39defb5d89dd43c5022d19dec6d0b'

rawdata=urllib2.urlopen(url)

jsondata=urllib2.urlopen(url)
jsondatastring=jsondata.read()
print jsondatastring
print "1---------------------"
dataload=json.load(rawdata)
print  dataload
print "2---------------------"
findvalue=dataload['name']
print findvalue
print "3---------------------"
datadumps=json.dumps(dataload)
print datadumps
print "4---------------------"
datadumpsraw=json.dumps(jsondatastring)
print datadumpsraw