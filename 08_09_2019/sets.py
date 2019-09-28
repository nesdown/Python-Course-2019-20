# * Sets are unordered
# * Set elements are unique
# * Кол-во элементов set может меняться, но сами элементы - нет

x = set(['foo', 'bar', 'hello', 'go', 'foo', 'bar'])
print(x)

x = set('hello world')
print(x)

x = {'o', 'b', 'k', 23, (1, 2, 3)}

{'foo'}
set('foo')

x = set()
print(type(x))

d = {}
print(type(d))

x = {'foo', 'bar', 'hello', 'go', 'foo', 'bar'}
print(len(x))

x1 = {'foo', 'bar', 'baz'}
x2 = {'baz', 'qux', 'quux'}
x3 = {'bark', 'meow'}
x4 = {'bom', 'bam', 'bim'}
# union
print(x1 | x2 | x3 | x4)
print(x1.union(x2, x3, x4))

# intersection
print(x1 & x2)
print(x1.intersection(x2))

# difference
print(x1 - x2)

# symmetric_difference
print(x1 ^ x2)
print(x1.symmetric_difference(x2))

x1.isdisjoint(x2)
x1.issubset(x2)
x1.issuperset(x2)
x1 > x2
x1 < x2

x1.add()
x1.remove()
