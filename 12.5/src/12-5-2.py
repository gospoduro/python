#Sample problem: http://py4e-data.dr-chuck.net/known_by_Fikret.html
#Actual problem: http://py4e-data.dr-chuck.net/known_by_Joris.html

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
#
url = input('Enter URL: ')
#if (len(url) < 1): url = "http://py4e-data.dr-chuck.net/known_by_Fikret.html"
if (len(url) < 1): url = "http://py4e-data.dr-chuck.net/known_by_Joris.html"
numimp = int(input('Enter the number of times to repeat: '))
posimp = int(input('Enter the item number to search: ')) - 1
#
for num in range(numimp) :
    html = urllib.request.urlopen(url).read()
    #html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    print('Retrieving:', url)
    url = tags[posimp].get('href', None)
#    
print('Retrieving:', url)


'''
Sample problem: Start at http://py4e-data.dr-chuck.net/known_by_Fikret.html
Find the link at position 3 (the first name is 1). Follow that link. Repeat this process 4 times. The answer is the last name that you retrieve.
Sequence of names: Fikret Montgomery Mhairade Butchi Anayah
Last name in sequence: Anayah
Actual problem: Start at: http://py4e-data.dr-chuck.net/known_by_Joris.html
Find the link at position 18 (the first name is 1). Follow that link. Repeat this process 7 times. The answer is the last name that you retrieve.
Hint: The first character of the name of the last page that you will load is: L
'''