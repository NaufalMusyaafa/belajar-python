data = "ini adalah string"
print(data)
print(type(data))

# 1. cara membuat string

"""
    1. menggunakan single quote'...'
    2. menggunakan double quote "..."
    3. menggunakan tanda \
"""

data = 'menggunakan singel quote'
print(data)
data = "menggunakan double quote"
print(data)

print('"hallo, apa kabar?"')
print("'hallo, apa kabar?'")
print("ini adalah hari jum'at")

# membuat tanda ' menjadi string
print('mari shalat jum\'at')
print('g\' day, isn\'t it?')

# backslash
print("C:\\user\\Ucup")

# tab
print('ucup\t, ocong, taruhan datang', "taruhan dapat siapa yang memiliki kursi nasional")

# backspace
print("ucup \botong")

# newline
print("baris pertama.\nbaris kedua.") # LF -> line feed -> dipakai oleh macOS, linux
print("baris pertama.\rbaris kedua.") # CR -> carriage return -> dipakai oleh commodore, acorn, lisp
print("baris pertama.\r\nbaris kedua.") #CRLF -> line feed carriage return -> dipakai oleh windows

# 3. string literal / raw

# hati-hati
print('C:\new folder') #akan salah pathnya

# menggunakan raw string
print(r'C\new folder \t')

# multiline literal string
print("""
Nama : ucup
Kelas : 3 SD""")

# multiline literal string dan raw
print(r"""
Nama : ucup
Kelas : 3 SD
website : www.newid.com/newID""")
