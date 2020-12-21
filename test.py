#! /usr/bin/env python3

a = 3
b = 4
print(a/b)
print(a//b)

multiline = """test
multiline"""
print(multiline)

color = "red"
print("the ball is %s." % (color))

x = 4
print(3 < x < 5) # chain the less than. return True

x = [1, 2, 3]
print(5 in x)
print(3 in x)

car = {'model': 'Chevy', 'year': 1970, 'color': 'red'}
if 'color' in car:
  print('This is a {0} car'.format(car['color']))

pets = ['cat', 'dog', 'dog']
print(pets.count('dog'))
pets.remove('dog')
print(pets)
print(pets.count('dog'))


# slice list
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(a[2:5])
print(a[2:])
print(a[:5])
print(a[-3:])
a[2:5] = ['foo', 'bar', 'baz']
print(a)

# powerful list comprehensions
zoo_animals = ['elephant', 'frog', 'tiger', 'cat']
my_animals = ['frog', 'cat']
other_animals = [
  animal
  for animal in zoo_animals
  if animal not in my_animals
]
print(other_animals)

# tuple is immutable list (similar to typescript)
t = 'dog', 'cat', 12345
print(t)
print(id(t))
t = 'dog', 'cat', 12345, 'foo'
print(t)
print(id(t))

# set, only allow unique key
s = {'a', 'd', 'c', 'a', 'f'}
print(s)
newSet = set()
newSet.add('t')
print(newSet)
newSet.add('a')
print(newSet.union(s))