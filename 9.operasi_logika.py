# not, or, and, xor

# not
print('====NOT====')

a = True
c = not a
print('data a =', a)
print('data c =', c)

# or
print("====OR====")
a = True
b = True
c = a or b
print(a, 'or', b, '=', c)
a = True
b = False
c = a or b
print(a, 'or', b, '=', c)
a = False
b = True
c = a or b
print(a, 'or', b, '=', c)
a = False
b = False
c = a or b
print(a, 'or', b, '=', c)

# and
print("====AND====")
a = True
b = True
c = a and b
print(a, 'and', b, '=', c)
a = True
b = False
c = a and b
print(a, 'and', b, '=', c)
a = False
b = True
c = a and b
print(a, 'and', b, '=', c)
a = False
b = False
c = a and b
print(a, 'and', b, '=', c)

# XOR
print("====XOR====")
a = True
b = True
c = a ^ b
print(a, 'XOR', b, '=', c)
a = True
b = False
c = a ^ b
print(a, 'XOR', b, '=', c)
a = False
b = True
c = a ^ b
print(a, 'XOR', b, '=', c)
a = False
b = False
c = a ^ b
print(a, 'XOR', b, '=', c)