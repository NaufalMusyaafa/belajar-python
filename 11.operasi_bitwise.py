#operator bitwise, operasi biner/binary

a = 9
b = 5

# bitwise or (|)
c = a | b
print("=====OR=====")
print("nilai :", a, " , binary :", format(a, "08b"))
print("nilai :", b, " , binary :", format(b, "08b"))
print("-------------------------------- (|)")
print("nilai :", c, " , binary :", format(c, "08b"))

# bitwise and (&)
c = a & b
print("\n=====AND=====")
print("nilai :", a, " , binary :", format(a, "08b"))
print("nilai :", b, " , binary :", format(b, "08b"))
print("-------------------------------- (&)")
print("nilai :", c, " , binary :", format(c, "08b"))

# bitwise xor (^)
c = a ^ b
print("\n=====XOR=====")
print("nilai :", a, " , binary :", format(a, "08b"))
print("nilai :", b, " , binary :", format(b, "08b"))
print("-------------------------------- (^)")
print("nilai :", c, " , binary :", format(c, "08b"))

# bitwise not (~)
print("\n=====NOT=====")
c = ~a
print("nilai :", a, " , binary :", format(a, "08b"))
print("-------------------------------- (~)")
print("nilai :", c, " , binary :", format(c, "08b")) 
#nilai not dari 9 = -(9+1) atau nilai not dari a = -(a+1)
print("-------------------------------- (^)")
d = 0b0000001001
e = 0b1111111111
print("nilai :", d^e, ", binary :", format(d^e, "08b")) #mirror dari ~a

# shifting

# shift right (>>)
print("\n=====>>=====")
c = a >> 1 #menggeser biner 1 sebanyak 1 kali
print("nilai :", a, " , binary :", format(a, "08b"))
print("-------------------------------- (>>)")
print("nilai :", c, " , binary :", format(c, "08b")) 

# shift left (<<)
print("\n=====<<=====")
c = a << 1
print("nilai :", a, " , binary :", format(a, "08b"))
print("-------------------------------- (<<)")
print("nilai :", c, " , binary :", format(c, "08b")) 