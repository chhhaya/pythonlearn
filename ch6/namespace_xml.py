from xml.etree.ElementTree import parse, iterparse

doc = parse('namespace.xml')
print(doc.findtext('author'))
print(doc.find('content'))
print(doc.find('content/html'))
# None
print(doc.find('content/{http://www.w3.org/1999/xhtml}html'))
# find
print(doc.find('content/{http://www.w3.org/1999/xhtml}html/head/title'))
# None
print(doc.find('content/{http://www.w3.org/1999/xhtml}html/'
               '{http://www.w3.org/1999/xhtml}head/'
               '{http://www.w3.org/1999/xhtml}title'))
# find

class XMLNamespaces:
    def __init__(self, **kwargs):
        self.namespaces = {}
        for name, uri in kwargs.items():
            self.register(name, uri)

    def register(self, name, uri):
        self.namespaces[name] = '{' + uri + '}'

    def __call__(self, path):
        return path.format_map(self.namespaces)

ns = XMLNamespaces(html='http://www.w3.org/1999/xhtml')
print(doc.find(ns('content/{html}html')))
# find
print(doc.findtext(ns('content/{html}html/{html}head/{html}title')))
# Hello world
print('--'*10)
for evt, elem in iterparse('namespace.xml', ('start', 'end', 'start-ns', 'end-ns')):
    print(evt, elem)
# end <Element 'author' at 0x102231098>
# start-ns ('', 'http://www.w3.org/1999/xhtml')
# end <Element '{http://www.w3.org/1999/xhtml}title' at 0x102231228>
# end <Element '{http://www.w3.org/1999/xhtml}head' at 0x1022311d8>
# end <Element '{http://www.w3.org/1999/xhtml}h1' at 0x1022312c8>
# end <Element '{http://www.w3.org/1999/xhtml}body' at 0x102231278>
# end <Element '{http://www.w3.org/1999/xhtml}html' at 0x102231188>
# end-ns None
# end <Element 'content' at 0x1022310e8>
# end <Element 'top' at 0x10222cf98>

### 推荐用lxml库，能处理复杂情况