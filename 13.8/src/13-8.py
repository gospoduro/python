#Sample data: http://py4e-data.dr-chuck.net/comments_42.json (Sum=2553)
#Actual data: http://py4e-data.dr-chuck.net/comments_115641.json (Sum ends with 70)
import urllib.request, urllib.parse, urllib.error
import json
#
url = input('Enter location: ')
#if (len(url) < 1): url = "http://py4e-data.dr-chuck.net/comments_42.json"
if (len(url) < 1): url = "http://py4e-data.dr-chuck.net/comments_115641.json"
print('Retrieving', url)
#
data = urllib.request.urlopen(url).read().decode('utf-8')
print('Retrieved', len(data), 'characters')
#
info = json.loads(data)
sum = 0
counts = 0
comments = info["comments"]
#
for comment in comments :
    sum += int(comment["count"])
    counts += 1
#
print('Count:', counts)
print('Sum:', sum)



'''
{
  comments: [
    {
      name: "Matthias"
      count: 97
    },
    {
      name: "Geomer"
      count: 97
    }
    ...
  ]
}
'''
'''
$ python3 solution.py
Enter location: http://py4e-data.dr-chuck.net/comments_42.json
Retrieving http://py4e-data.dr-chuck.net/comments_42.json
Retrieved 2733 characters
Count: 50
Sum: 2...
'''