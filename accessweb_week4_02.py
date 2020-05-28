import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

#SSL Certification Error Handle
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#Data Collection
link = input('Enter URL: ')
count = int(input('Enter count: '))
pos = int(input('Enter position: '))

print('Retrieving:', link)

for i in range(count):
    html = urllib.request.urlopen(link, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a') #finding the anchor tags
    x = 0 #to compare position
    for tag in tags:
        x += 1
        if x == pos:
            link = str(tag.get('href', None))
            print('Retrieving:', link)
            x = 0 #restarting 
            break #breaking because once position is found, no need to go fwd

# Enter URL: http://py4e-data.dr-chuck.net/known_by_Ama.html
# Enter count: 7
# Enter position: 18