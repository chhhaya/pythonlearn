from xml.etree.ElementTree import Element

# 字典转xml
def dict_to_xml(tag, d):
    elem = Element(tag)
    for key, val in d.items():
        child = Element(key)
        child.text = str(val)
        elem.append(child)
    return elem

s = {'name': 'Good', 'shares': 100, 'price': 280.2}
e = dict_to_xml('stock', s)
print(e)

# xml 转string
from xml.etree.ElementTree import tostring
print(tostring(e))

# 增加属性：
e.set('_id', '1234')
print(tostring(e))

#如果只需要变成string类型的xml
def dict_to_xml_str(tag, d):
    parts = ['<{}>'.format(tag)]
    for key, val in d.items():
        parts.append('<{0}>{1}<{0}>'.format(key, val))
    parts.append('</{}>'.format(tag))
    return ''.join(parts)

e = dict_to_xml_str('stock', s)
print(e)
# <stock><shares>100<shares><price>280.2<price><name>Good<name></stock>
# 如果字典的值带特殊字符：
s = {'name': '<spam>'}
e = dict_to_xml_str('item', s)
print(e)
# 原封不动给输出来了
# <item><name><spam><name></item>

e = dict_to_xml('item', s)
print(tostring(e))
# b'<item><name>&lt;spam&gt;</name></item>'
# xml的给帮转义了

# 如果要自己手动转义
from xml.sax.saxutils import escape, unescape
print(escape('<spam>'))
# &lt;spam&gt;
print(unescape('&lt;spam&gt;'))
# <spam>