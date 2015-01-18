from urllib.request import urlopen
import csv


def urlprint(protocol, host, domain):
    url = '{}://{}.{}'.format(protocol, host, domain)
    print(url)


def func(x):
    return x


def dowprices():
    u = urlopen('http://finance.yahoo.cmd/d')
    lines = (line.decode('utf-8') for line in u)
    rows = (row for row in csv.reader(lines) if len(row) == 2)
    prices = {name: float(price) for name, price in rows}
    return prices