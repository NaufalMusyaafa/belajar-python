# program konversi calcius ke satuan lain

print("PROGRAM KONVERTASI TEMPERATUR\n ")

celcius = float(input("Masukkan suhu dalam celcius : "))
print("Suhu adalah :", celcius, "celcius")

# Reamur

reamur = (4/5) * celcius
print("Suhu", celcius, "dalam reamur adalah", reamur, "reamur")

# Fahrenheit

fahrenheit = ((9/5) * celcius) + 32
print("Suhu", celcius, "dalam fahrenheit adalah", fahrenheit, "fahrenheit")

# Kelvin

kelvin = celcius + 273
print("Suhu", celcius, "dalam kelvin adalah", kelvin, "kelvin\n")

# konversi fahrenheit ke kelvin

print("PROGRAM KONVERTASI TEMPERATUR FAHRENHEIT KE KELVIN\n ")
fahrenheit = float(input("Masukkan suhu dalam fahrenheit : "))
kelvin = (((5/9) * (fahrenheit - 32)) + 273)
print("Suhu", fahrenheit, "dalam kelvin adalah", kelvin, "kelvin")

# konversi kelvin ke fahrenheit

print("PROGRAM KONVERTASI TEMPERATUR KELVIN  KE FAHRENHEIT\n ")
kelvin = float(input("Masukkan suhu dalam kelvin : "))
fahrenheit = (((kelvin - 273) *(9/5)) + 32)
print("Suhu", kelvin, "dalam fahrenheit adalah", fahrenheit, "fahrenheit")
