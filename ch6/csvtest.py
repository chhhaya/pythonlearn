import csv

# 写CSV (tuple)
# 默认写进去是逗号分隔的，用number打开正常，用excel打开不正常。
# writer时指定delimiter为分号再写，excel打开就正常了
# 同时reader的时候也要指定delimiter为分号
headers = ['Symbol', 'Price', 'Date', 'Time', 'Change', 'Volume']
rows = [('AA', 39.48, '6/11/2011', '9:36am', -0.18, 181800),
        ('AIG', 39.48, '6/11/2011', '9:36am', -0.18, 181800),
        ('AXP', 39.48, '6/11/2011', '9:36am', -0.18, 181800),
        ('ABC', 39.48, '6/11/2011', '9:36am', -0.18, 181800),
        ('ES', 39.48, '6/11/2011', '9:36am', -0.18, 181800)
        ]
with open('stock.csv', 'w') as f:
    print(dir(csv))
    f_csv = csv.writer(f, delimiter=';')
    f_csv.writerow(headers)
    f_csv.writerows(rows)

# 写CSV (dict)
rows2 = [{'Symbol': 'AA', 'Price':39.48, 'Date':'6/11/2011', 'Time':'9:36am', "Change":-0.18, 'Volume':81800},
{'Symbol': 'A G', 'Price':39.48, 'Date':'6/11/2011', 'Time':'9:36am', "Change":-0.18, 'Volume':181800},
{'Symbol': 'AX', 'Price':39.48, 'Date':'6/11/2011', 'Time':'9:36am', "Change":-0.18, 'Volume':181800},
{'Symbol': 'AC', 'Price':39.48, 'Date':'6/11/2011', 'Time':'9:36am', "Change":-0.18, 'Volume':181800},
{'Symbol': 'ES', 'Price':39.48, 'Date':'6/11/2011', 'Time':'9:36am', "Change":-0.18, 'Volume':181800}]

with open('stock2.csv', 'w') as f:
    f_csv = csv.DictWriter(f, headers)
    f_csv.writeheader()
    f_csv.writerows(rows2)

# 读CSV
import re
col_types = [str, float, str, str, float, int]
with open('stock2.csv') as f:
    f_csv = csv.reader(f, delimiter=',')
    # 如果header中带特殊字符的话，需要转成合法的才能读
    headers = [re.sub('[^a-zA-Z_]', '_', h) for h in next(f_csv)]
    print(headers)
    for row in f_csv:
        # 默认都是字符串， 需要自己转换类型
        row = tuple(convert(value) for convert, value in zip(col_types, row))
        print(row)

# 用namedtuple读
from collections import namedtuple
with open('stock2.csv') as f:
    f_csv = csv.reader(f)
    headers = next(f_csv)
    Row = namedtuple('Row', headers)
    for r in f_csv:
        row = Row(*r)
        #print(row.Symbol, row.Time)
        print(row)