"""
stack = suatu susunan data dimana data dapat ditambah dan dihapus selalu dilakukan pada bagian akhir data, yang disebut dengan top of stack

stack bersifat LIFO (last in first out)

push: menambah item pada stack pada tumpukan paling atas
pop: mengambil item pada stack pada tumpukan paling atas
clear: mengosongkan stack
isEmpty: mengecek apakah stack sudah kosong
IsFull: mengecek apakah stack sudah penuh
"""

from collections import queue

stack = []

stack.append('a')
stack.append('b')
stack.append('c')
stack.append('d')
stack.append('e')

print("initial stack")
print(stack)

print("element yang di keluar dari stack")
print(stack.pop())
print(stack)

print(stack.pop())
print(stack)

#deque
queue = []

queue.que = (10)
queue.que = (20)
queue.que = (30)
queue.que = (40)

print("initial queue")
print(queue)

print("element yang keluar dari queue")
print(queue)