#casting adalah merubah dari satu tipe ke tipe lain
#tipe data = int, float, string, boolean

# INTEGER
print("==================INTEGER==================")
data_int = -1
print("Data = ", data_int, " type datanya adalah = ", type(data_int))
data_float_dari_int = float(data_int)
print("Data = ", data_float_dari_int, " type datanya adalah = ", type(data_float_dari_int))


# FLOAT
print("==================FLOAT==================")
data_float = 9.5
print("Data = ", data_float, " type datanya adalah = ", type(data_float))
data_int_dari_float = int(data_float) #akan dibulatkan ke bawah
print("Data = ", data_int_dari_float, " type datanya adalah = ", type(data_int_dari_float)) 


# BOOLEAN
print("==================BOOLEAN==================")
data_bool = False
print("Data = ", data_bool, " type datanya adalah = ", type(data_bool))
data_float_dari_bool = float(data_bool)
print("Data = ", data_float_dari_bool, " type datanya adalah = ", type(data_float_dari_bool))


# INTEGER
print("==================STRING==================")
data_string = ""
# print("Data = ", data_string, " type datanya adalah = ", type(data_string))
# data_float_dari_integer = float(data_string)
# print("Data = ", data_float_dari_integer, " type datanya adalah = ", type(data_float_dari_integer))
data_bool_dari_string = bool(data_string)
print("Data = ", data_bool_dari_string, " type datanya adalah = ", type(data_bool_dari_string))



# data_string = str(data_int)
# data_bool = bool(data_int) #akan false jika nilai integer = 0
# print("Data = ", data_string, " type datanya adalah = ", type(data_string))
# print("Data = ", data_bool, " type datanya adalah = ", type(data_bool))