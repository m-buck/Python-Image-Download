import urllib
import urllib2
import requests

url = 'http://192.168.1.22/picture/1/current/'

#print "downloading with urllib2"
f = urllib2.urlopen(url)
data = f.read()
with open("image.png", "wb") as code:
    code.write(data)