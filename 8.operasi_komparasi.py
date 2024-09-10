# setiap hasil dari operasi komparasi adalah boolean

# >, <, >=, <=, ==, !=, , is, is not

a = 4
b = 2

# lebih besar dari >
print("LEBIH BESAR DENGAN >")

hasil = a > 1
print(a, '>', 2, '', hasil)
print(a, '>', 4, '', hasil)
print(a, '>', -1, '', hasil)

# lebih besar dari >

print("LEBIH KECIL DENGAN <")

hasil = a < 5
print(a, '<', 5, '', hasil)
hasil = a < 4
print(a, '<', 4, '', hasil)
hasil = a < -1
print(a, '<', -1, '', hasil)

# sama dengan ==

hasil = a == 5
print(a, '==', 5, '', hasil)
hasil = a == 4
print(a, '==', 4, '', hasil)
hasil = a == -1
print(a, '==', -1, '', hasil)

# tidak sama dengan !=

hasil = a != 5
print(a, '!=', 5, '', hasil)
hasil = a != 4
print(a, '!=', 4, '', hasil)
hasil = a != -1
print(a, '!=', -1, '', hasil)

print("OBJECT IDENTITY (is)")

# > <  >= <= == != dapat bekerja pada syntax literal
a == 4 # 4 adalah literal, a ada memory sedangkan 4 tidak

# is digunakan untuk membandingkan memory/object (komparasi object identity)

x = 5 #assigment membuat object
y = 5
print('nilai x =', x, ', id = ', hex(id(x)))
print('nilai y =', y, ', id = ', hex(id(y)))

hasil = x is y
print("x is y = ", hasil)

print("OBJECT IDENTITY (is not)")

x = 5 #assigment membuat object
y = 6
print('nilai x =', x, ', id = ', hex(id(x)))
print('nilai y =', y, ', id = ', hex(id(y)))

hasil = x is not y
print("x is not y = ", hasil)