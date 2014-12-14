import csv

# 写CSV (tuple)
headers = ['Symbol', 'Price', 'Date', 'Time', 'Change', 'Volume']
rows = [('AA', 39.48, '6/11/2011', '9:36am', -0.18, 181800),
        ('AIG', 39.48, '6/11/2011', '9:36am', -0.18, 181800),
        ('AXP', 39.48, '6/11/2011', '9:36am', -0.18, 181800),
        ('ABC', 39.48, '6/11/2011', '9:36am', -0.18, 181800),
        ('ES', 39.48, '6/11/2011', '9:36am', -0.18, 181800)
        ]
# with open('stock.csv', 'w') as f:
#     print(dir(csv))
#     f_csv = csv.writer(f)
#     f_csv.writerow(headers)
#     f_csv.writerows(rows)

# 写CSV (dict)
rows2 = [{'Symbol': 'AA', 'Price':39.48, 'Date':'6/11/2011', 'Time':'9:36am', "Change":-0.18, 'Volume':'181800'},
{'Symbol': 'AG', 'Price':39.48, 'Date':'6/11/2011', 'Time':'9:36am', "Change":-0.18, 'Volume':'181800'},
{'Symbol': 'AX', 'Price':39.48, 'Date':'6/11/2011', 'Time':'9:36am', "Change":-0.18, 'Volume':'181800'},
{'Symbol': 'AC', 'Price':39.48, 'Date':'6/11/2011', 'Time':'9:36am', "Change":-0.18, 'Volume':'181800'},
{'Symbol': 'ES', 'Price':39.48, 'Date':'6/11/2011', 'Time':'9:36am', "Change":-0.18, 'Volume':'181800'}]

with open('stock2.csv', 'w') as f:
    f_csv = csv.DictWriter(f, headers)
    f_csv.writeheader()
    f_csv.writerows(rows2)

# 读CSV
with open('stock.csv') as f:
    f_csv = csv.reader(f)
    headers = next(f_csv)
    print(headers)
    for row in f_csv:
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