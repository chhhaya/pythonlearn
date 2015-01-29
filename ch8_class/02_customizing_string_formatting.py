_formats = {
    'ymd': '{d.year}-{d.month}-{d.day}',
    'mdy': '{d.month}/{d.day}/{d.year}',
    'dmy': '{d.day}/{d.month}/{d.year}'
    }

class Date:
    def __init__(self, year, month, day):
        self.month = month
        self.year = year
        self.day = day

    def __format__(self, format_spec):
        if format_spec == '':
            format_spec = 'ymd'
        fmt = _formats[format_spec]
        return fmt.format(d=self)

d = Date(2015, 9, 20)
print(format(d))
# 2015-9-20
print(format(d, 'mdy'))
# 9/20/2015
print('The date is {:mdy}'.format(d))
# The date is 9/20/2015

# datetime模块中的format

from datetime import date
d = date(2013, 2, 3)
print(format(d))
# 2013-02-03
print(format(d, '%A, %B %d, %Y'))
# Sunday, February 03, 2013
print('The end is {:%d %b %Y}. good bye'.format(d))
# The end is 03 Feb 2013. good bye