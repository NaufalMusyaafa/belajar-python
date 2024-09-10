# 1. menyambung string (concatenate)
nama_pertama = "Ucup"
nama_tengah = "D"
nama_akhir = "Fame"

nama_lengkap = nama_pertama + " " + nama_tengah  + "'"+ nama_akhir
print("nama lengkap : " + nama_lengkap)

# 2. menghitung panjang dari string
panjang = len(nama_lengkap)
print("Panjang dari " + nama_lengkap + " = " + str(panjang))

# 3. operator untuk string

# mengecek apakah ada komponen karakter/string pada string
d = "d"
status = d in nama_lengkap # case sensitive
print(d + " ada di" + nama_lengkap + " = " + str(status))

D = "D"
status = D in nama_lengkap
print(D + " ada di" + nama_lengkap + " = " + str(status))

d = "d"
status = d not in nama_lengkap
print(d + " tidak ada di" + nama_lengkap + " = " + str(status))

# mengulang string
print("==" * 10)
print(10 * "wk" * 2)

# indexing
print("index ke-0 : " + nama_lengkap[0]) #index dimulai dari 0
print("index ke-1 : " + nama_lengkap[1])
print("index ke-6 : " + nama_lengkap[6])
print("index ke-(-1) : " + nama_lengkap[-1])
print("index ke-(-2) : " + nama_lengkap[-2])
print("index ke-[0-3] : " + nama_lengkap[0:4]) #index terakhir tidak diambil
print("index ke-[3-7] : " + nama_lengkap[3:8])
print("index ke-[0,2,4,6,8,10] : " + nama_lengkap[0:10:2]) # index 0 sampai 10 dengan increment 2

# item paling kecil (dihitung berdasarkan nilai ASCII code nya)
print("Paling kecil : " + min(nama_lengkap))

# item paling besar (dihitung berdasarkan nilai ASCII code nya)
print("Paling besar : " + max(nama_lengkap)) 
ascii_code = ord(" ")

print("ASCII code untuk spasi adalah " + str(ascii_code))
data = 117
print("char untuk ASCII 117 adalah " + chr(data))

# 4. operator dalam bentuk method
data = "otong surotong pararotong"
jumlah = data.count("o") # data adalah object dan count adalah methodnya
print("jumlah o pada " + data + " adalah " + str(jumlah) )

<<<<<<< HEAD
=======
# merubah case dari string

# merubah semua ke upper case

salam = "Assalamu'alaikum"
print("normal = " + salam)
salam = salam.upper() 
print("upper = " + salam)


# merubah semua ke lower case

salam = "AssalamU'AlaIkUm"
print("normal = " + salam)
salam = salam.lower() 
print("upper = " + salam)

# pengecekan dengan isX method

# contoh untuk pengecekan lower case
salam = "assalamu'alaikum"
apakah_lower = salam.islower() #hasilnya bool
print(salam + " is lower = " + str(apakah_lower))
apakah_upper = salam.isupper()
print(salam + " is lower = " + str(apakah_upper))

# isalpha() = untuk mengecek apakah semuanya huruf (huruf dan angka)
# isdecimal() = untuk angka saja
# isspace() = spasi, tab, newline(\n)
# istitle = semua kata dimulai dengan huruf besar

judul = "It's Okay Not To Be Dynasty"
cek_judul = judul.istitle()
print(judul + " is title = " + str(cek_judul))

# mengecek komponen startswith() endwith()
cek_start = "Start kang".startswith("Start")


>>>>>>> abf9b3f489c460eeff43509ae3b55ded680b4e30
"""
Perbedaan + dan , pada string
+ bisa digunakan untuk menambah nilai dari suatu variabel sedangkan , tidak
, menambahkan spasi pada output sedangkan + tidak
"""