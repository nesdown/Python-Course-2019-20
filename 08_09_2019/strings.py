s = "hello"
print(s*-4)

print(chr(123))
print(ord('c'))

# i = -6-5-4-3-2-1
s = 'foobar'
# i = 012345

s[0]
s[len(s) - 1]
s[-3]
print(s[2:5])
print(s[:4])
print(s[2:])

t = s[:]
print(id(s))
print(id(t))

print(s[1:-2])
print(s[0:6:2])
print(s[::2])
print(s[::-2])
print(s[::-1])

n = 20
m = 25
print('The product of', n, 'and', m, 'is', n*m)
print(f'The product of {n} and {m} is {n*m}')

# ОШИБКА
# s = 'foobar'
# s[3] = 'x'

s = s[:3] + 'x' + s[4:]
print(s)
s = 'FooBbBar'
s = s.replace('b', 'x')
print(s.swapcase())

s = s.capitalize()

s = "What's happened to ted's IBM stock?"
print(s.title())

print(s.count('p', 0, 8))
print(s.endswith('!'))
print(s.rfind('p'))
# print(s.index('j'))

s = 'abc123'
print(s.isalnum())
print(s.isalpha())
print(s.isdigit())

print('and'.isidentifier())
s = 'adhfjhkd \n hdasfhdsf \t'.isprintable()
s = "\n \t \v"
s.isspace()

s = 'foo'
print('h'.center(10, '-'))
print('e'.center(10, '-'))
print('l'.center(10, '-'))
print('l'.center(10, '*'))
print('o'.center(10, '&'))

s = 'a\tb\tc'
print(s.expandtabs(20))

s = 'fooobar'
print(s.replace('o', 'x', 2))

m = ['hello', 'bye', 'good', 'bad', 'cool']
s = ', '.join(m)
print(str(m))
print(list('hello world'))
s = 'foo..bar..hello'
print(s.rpartition('..'))
print('www.z-digital.net'.split('.', 1))
