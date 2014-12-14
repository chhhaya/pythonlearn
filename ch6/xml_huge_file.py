from xml.etree.ElementTree import iterparse
from xml.etree.ElementTree import parse
from collections import Counter

def parse_and_remove(filename, path):
    path_parts = path.split('/')
    doc = iterparse(filename, ('start', 'end'))
    next(doc)
    tag_stack = []
    elem_stack = []
    for event, elem in doc:
        if event == 'start':
            tag_stack.append(elem.tag)
            elem_stack.append(elem)
        elif event == 'end':
            if tag_stack == path_parts:
                yield elem
                elem_stack[-2].remove(elem)
            try:
                tag_stack.pop()
                elem_stack.pop()
            except IndexError:
                pass

potholes_by_link = Counter()
# doc = parse('rss20.xml')
# for pothole in doc.iterfind('channel/item'):
#     potholes_by_link[pothole.findtext('link')] += 1

data = parse_and_remove('rss20.xml', 'channel/item')
for pothole in data:
    potholes_by_link[pothole.findtext('link')] += 1

for zipcode, num in potholes_by_link.most_common():
    print(zipcode, num)


# >>> from xml.etree.ElementTree import iterparse
# >>> data = iterparse('rss20.xml', ('start', 'end'))
# >>> next(data)
# ('start', <Element 'rss' at 0x1026e5278>)
# >>> next(data)
# ('start', <Element 'channel' at 0x1026e5228>)
# >>> next(data)
# ('start', <Element 'title' at 0x1026e5368>)
# >>> next(data)
# ('end', <Element 'title' at 0x1026e5368>)