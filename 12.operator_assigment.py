# operasi yg dapat dilakukan dengan penyingkatan
# operasi ditambah dengan assigment

a = 5 # ini adalah assigment
print("nilai a =", a)

a += 1 # artinya sama dengan a = a + 1
print("nilai a+= 1, maka nilai a menjadi", a)

a -= 2 # artinya sama dengan a = a - 2
print("nilai a-= 2, maka nilai a menjadi", a)

a *= 5 # artinya sama dengan a = a * 2
print("nilai a*= 5, maka nilai a menjadi", a)

a /= 2 # artinya sama dengan a = a / 2
print("nilai a/= 2, maka nilai a menjadi", a)

# Modulus dan floor division
b = 10
print("\nnilai b =", b)

b %= 3
print("nilai b %= 3, maka nilai b menjadi", b)

b = 10
print("\nnilai b =", b)

b //= 3
print("nilai b //= 3, maka nilai b menjadi", b)

b = 5
print("\nnilai b =", b)

# pangkat/eksponen
b **= 3
print("nilai b **= 3, maka nilai b menjadi", b)

# operasi bitwise
# or 
c = False
print("\nnilai c =", c)

c |= True
print("nilai c |= False, maka nilai c menjadi", c)

# and
c = True
print("\nnilai c =", c)

c &= False
print("nilai c &= True, maka nilai c menjadi", c)

# xor
c = True
print("\nnilai c =", c)

c ^= False
print("nilai c ^= False, maka nilai c menjadi", c)

# penggeseran
d = 0b00100
print("\nnilai d =", format(d, "04b"))
d >>= 2
print("nilai d >>= 2, maka nilai d menjadi", format(d, "04b"))
d <<= 1
print("nilai d <<= 1, maka nilai d menjadi", format(d, "04b"))