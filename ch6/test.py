from urllib.request import urlopen
from xml.etree.ElementTree import parse

u = urlopen('http://planetpython.org/rss20.xml')
doc = parse(u)
