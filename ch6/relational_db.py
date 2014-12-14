stocks = [
    ('GOOD', 100, 490.1),
    ('AAPL', 50, 545.75),
    ('FB', 150, 7.34),
    ('HPB', 65, 22.3),
]
import sqlite3
db = sqlite3.connect('stock.db')
c = db.cursor()
c.execute("CREATE TABLE portfolio(symbol text, shares integer, price real)")
db.commit()
c.executemany('INSERT INTO portfolio VALUES(?, ?, ?)', stocks)
db.commit()

for row in db.execute("SELECT * FROM portfolio"):
    print(row)
db.close()