import  urllib2
a=urllib2.urlopen("https://www.w3schools.com/xml/plant_catalog.xml")
text=a.read()
a=str(text)
print a.strip("<C4AT")


# for i in text:
#     if "COMMON" in i:
#
#         print i.strip("<")