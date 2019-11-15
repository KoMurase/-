import collections
l = ['a', 'a', 'a', 'a', 'b', 'c', 'c']

print([i for i in l if l.count(i) >= 2])
print(len([i for i in l if l.count(i) >= 2]))

c = collections.Counter(l)
print([i[0] for i in c.items() if i[1] >= 2])

print(len([i[0] for i in c.items() if i[1] >= 2]))


"""
['a', 'a', 'a', 'a', 'c', 'c']
6
['a', 'c']
2
"""
