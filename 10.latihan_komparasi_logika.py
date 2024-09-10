# membuat gabungan area rentang dari angka

#+++++3-----10+++++

inputUser = float(input('masukkan angka yang bernilai\nkurang dari 3\natau lebih dari 10: '))

#+++++3-----
# memeriksa angka kurang dari 3
isKurangDari = (inputUser < 3)
print("kurang dari 3 =", isKurangDari)

#-----10+++++
# memeriksa angka lebih dari 10
isLebihDari = (inputUser > 10)
print("lebih dari 10 =", isLebihDari)

#+++++3-----10+++++

isCorrect = isKurangDari or isLebihDari
print("angka yang anda masukkan =", isCorrect)


#-----3+++++10-----
print("\n", 20 * "=", "\n")

inputUser = float(input('masukkan angka bernilai\nkurang dari 3\ndan lebih dari 10: '))

#+++++3-----
# memeriksa angka kurang dari 3
isKurangDari = (inputUser > 3)
print("kurang dari 3 =", isKurangDari)

#-----10+++++
# memeriksa angka lebih dari 10
isLebihDari = (inputUser < 10)
print("lebih dari 10 =", isLebihDari)

#+++++3-----10+++++

isCorrect = isKurangDari and isLebihDari
print("angka yang anda masukkan =", isCorrect)

# latihan no-1

#-----0+++++5-----8+++++11-----
inputUser = float(input("masukkan nilai: "))

#0+++++
is0LebihDari = (inputUser > 0)
print("lebih dari 0 =", is0LebihDari)

#+++++5
is5KurangDari = (inputUser < 5)
print("kurang dari 5 =", is5KurangDari)

#8+++++
is8LebihDari = (inputUser > 8)
print("lebih dari 8 =", is8LebihDari)

#+++++11
is11KurangDari = (inputUser < 11)
print("kurang dari 11 =", is11KurangDari)

isCorrect = (is0LebihDari and is5KurangDari) or (is8LebihDari and is11KurangDari)
print("angka yang anda masukkan =", isCorrect)


# latihan no-2

#+++++0-----5+++++8-----11+++++
inputUser = float(input("masukkan nilai: "))

#+++++0
is0KurangDari = (inputUser < 0)
print("kurang dari 0 =", is0KurangDari)

#5+++++
is5LebihDari = (inputUser > 5)
print("lebih dari 5 =", is5LebihDari)

#+++++8
is8KurangDari = (inputUser < 8)
print("kurang dari 8 =", is8KurangDari)

#11+++++
is11LebihDari = (inputUser > 11)
print("lebih dari 11 =", is11LebihDari)

isCorrect = (is8KurangDari or (is5LebihDari and is8KurangDari) or is11LebihDari)
print("angka yang anda masukkan =", isCorrect)
