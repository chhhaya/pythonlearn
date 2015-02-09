from functools import total_ordering

class Room:
    def __init__(self, name, length, width):
        self.name = name
        self.length = length
        self.width = width
        self.square = self.length * self.width

# 用了total_ordering, 只要实现了__lt__, 它就给你实现__gt__, __ge__, __ne__几个
@total_ordering
class House:
    def __init__(self, name, style):
        self.name = name
        self.style = style
        self.rooms = list()

    @property
    def living_space(self):
        return sum(r.square for r in self.rooms)

    def add_room(self, room):
        self.rooms.append(room)

    def __str__(self):
        return '{}:{} square foot {}'.format(self.name,
                                             self.living_space,
                                             self.style)
    def __eq__(self, other):
        return self.living_space == other.living_space

    def __lt__(self, other):
        return self.living_space < other.living_space

h1 = House('h1', 'Cape')
h1.add_room(Room('Master beedroom', 14, 23))
h1.add_room(Room('living beedroom', 10, 23))
h1.add_room(Room('chufang', 10, 20))
h1.add_room(Room('keting', 20, 23))

h2 = House('h2', 'Ranch')
h2.add_room(Room('Master beedroom', 14, 23))
h2.add_room(Room('living beedroom', 10, 23))
h2.add_room(Room('chufang', 10, 20))
h2.add_room(Room('keting', 20, 23))

h3 = House('h3', 'Bus')
h3.add_room(Room('Master beedroom', 10, 23))
h3.add_room(Room('living beedroom', 10, 23))
h3.add_room(Room('chufang', 10, 20))
h3.add_room(Room('keting', 20, 23))
print(h1 < h2)
# False
print(h1 == h2)
# True
print(h3 < h1)
# True
print(min(h1, h2, h3))
# h3:1120 square foot Bus
print(max(h1, h2 ,h3))
# h1:1212 square foot Cape
