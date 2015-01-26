add = lambda x, y: x+y
print(add(2, 3))
print(add('hello ', 'world'))

names = ['Dav Des', 'Vria HUD', 'Aefs JHG', 'DDef HYD']
print(sorted(names, key=lambda name: name.split()[-1].lower()))
# ['Dav Des', 'Vria HUD', 'DDef HYD', 'Aefs JHG']
