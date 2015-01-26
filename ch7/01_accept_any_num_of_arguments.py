def avg(first, *args):
    return (first + sum(args)) / (1 + len(args))

print(avg(1, 2))
# 1.5
print(avg(1, 2, 3, 4))
# 2.5

import html
def make_element(name, value, **kwargs):
    keyvals = [' %s = "%s"' % item for item in kwargs.items()]
    attr_str = ''.join(keyvals)
    element = '<{name}{attrs}>{value}</name>'.format(
        name=name,
        attrs=attr_str,
        value=html.escape(value)
    )
    return element

print(make_element('item', 'Albatross', size='lalrge', quantity=6))
# <item size = "lalrge" quantity = "6">Albatross</name>
print(make_element('p', '<spam>'))
# <p>&lt;spam&gt;</name>

def anyargs(*args, **kwargs):
    print(args) # a tuple
    print(kwargs) # a dict

    