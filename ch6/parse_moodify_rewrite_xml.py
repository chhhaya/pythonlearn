from xml.etree.ElementTree import parse, Element
doc = parse('pred.xml')
root = doc.getroot()
# 删除两个元素
root.remove(root.find('sri'))
root.remove(root.find('cr'))
# 找到元素位置
root.getchildren().index(root.find('nm'))
# 1
# 新建元素
e = Element('spam')
e.text = 'This is a test'
# 插入元素
root.insert(2, e)
doc.write('newpred.xml', xml_declaration=True)
