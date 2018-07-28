#Sample data: http://py4e-data.dr-chuck.net/comments_42.xml (Sum=2553)
#Actual data: http://py4e-data.dr-chuck.net/comments_115640.xml (Sum ends with 20)
import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
#
url = input('Enter location: ')
#if (len(url) < 1): url = "http://py4e-data.dr-chuck.net/comments_42.xml"
if (len(url) < 1): url = "http://py4e-data.dr-chuck.net/comments_115640.xml"
print('Retrieving', url)
#
data = urllib.request.urlopen(url).read()
print('Retrieved', len(data), 'characters')
#
tree = ET.fromstring(data)
counts = tree.findall('.//count')   
print('Count:', len(counts))
#
sum = 0
for count in counts :
    sum += int(count.text)
print('Sum:', sum)
