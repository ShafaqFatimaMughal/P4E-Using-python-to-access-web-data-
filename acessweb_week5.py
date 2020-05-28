import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Accessing the data
link = input('Enter location: ')
html = urllib.request.urlopen(link).read().decode()
print('Retrieving', link)
print('Retrieved', len(html), 'characters')

# Data calculation
times = 0
summ = 0
tree = ET.fromstring(html)

# tags = tree.findall('comments/comment')
# for tag in tags:
#     times += 1
#     summ += int(tag.find('count').text)

#shorter that above method. no need to find comments...
counts = tree.findall('.//count')
for count in counts:
    times += 1
    summ += int(count.text)

print('Count:', times)
print('Sum:', summ)