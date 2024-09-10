#operasi aritmatika

a = 10
b = 3

#operasi tambah +
hasil = a + b
print(a, "+", b, "=", hasil)

#operasi kurang - 
hasil = a - b
print(a, "-", b, "=", hasil)

#operasi kali *
hasil = a * b
print(a, "*", b, "=", hasil)

#operasi bagi / 
hasil = a / b
print(a, "/", b, "=", hasil, "Tipe datanya adalah ", type(hasil)) #hasil bagi desimal langsung mengubah tipe data menjadi float

#operasi eksponen (pangkat) **
hasil = a ** b
print(a, "**", b, "=", hasil)

#operasi modulus (sisa bagi) %
hasil = a % b
print(a, "%", b, "=", hasil)

#operasi floor division (pembulatan dari bagi) //
hasil = a // b
print(a, "//", b, "=", hasil)

# prioritas operasi, operational presedence
""" Prioritas operasi:
    1. kurung()
    2. eksponen **
    3. Perkalian dkk * ** %
    4. Pertambahan dan kekurangan"""

x = 3
y = 2
z = 4

hasil = x ** y * (z + x) / y - y % z // x
print(x, "**", y, "*", "(",z, "+", x,")", "/", y, "-", y, "%", z, "//", x, "=", hasil)