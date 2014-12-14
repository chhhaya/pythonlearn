from urllib.request import urlopen
from xml.etree.ElementTree import parse

u = urlopen('http://planetpython.org/rss20.xml')
doc = parse(u)
# 寻找所有channel下面的item
for item in doc.iterfind('channel/item'):
    title = item.findtext('title')
    date = item.findtext('pubDate')
    link = item.findtext('link')
    print(title)
    print(date)
    print(link, end='\n\n')

e = doc.find('channel/title')
print(e)
# <Element 'title' at 0x102546ef8>
print(e.tag)
# title
print(e.text)
# Planet Python
e.get('some_attribute')
