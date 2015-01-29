class Date:
    __slots__ = ['year', 'month', 'day']
    def __init__(self, year, month, day):
        self.month = month
        self.day = day
        self.year = year