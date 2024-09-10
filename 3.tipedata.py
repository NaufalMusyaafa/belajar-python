# a = 10, dimana a adalah variabel dengan nilai 10

# tipe data angka satuan (integer)
data_integer = 1000
print("data : ", data_integer, )
print("bertipe data ", type(data_integer))

# tipe data desimal (float)
data_float = 1.3
print("data : ", data_float, )
print("bertipe data ", type(data_float))

# tipe data kumpulan kata (string)
data_string = "ucup"
print("data : ", data_string, )
print("bertipe data ", type(data_string))

# tipe data biner true/false (boolean)
data_bool = True
print("data : ", data_bool, )
print("bertipe data ", type(data_bool))

# tipe data khusus

#tipe data kompleks
data_complex = complex(5,6)
print("data : ", data_complex, )
print("bertipe data ", type(data_complex))

# tipe data dari bahasa C
from ctypes import c_double

data_c_double = c_double(10.5)
print("data : ", data_c_double, )
print("bertipe data ", type(data_c_double))