# # bubble sort
# def bubble_sort(arr):

#     # Outer loop to iterate through the list n times
#     for n in range(len(arr) - 1, 0, -1):

#         # Inner loop to compare adjacent elements
#         for i in range(n):
#             if arr[i] > arr[i + 1]:

#                 # Swap elements if they are in the wrong order
#                 swapped = True
#                 arr[i], arr[i + 1] = arr[i + 1], arr[i]


# # Sample list to be sorted
# arr = [39, 12, 18, 85, 72, 10, 2, 18]
# print("Unsorted list is:")
# print(arr)

# bubble_sort(arr)

# print("Sorted list is:")
# print(arr)

# # insertion sort

# # Function to sort array using insertion sort
# def insertionSort(arr):
#     for i in range(1, len(arr)):
#         key = arr[i]
#         j = i - 1

#         # Move elements of arr[0..i-1], that are
#         # greater than key, to one position ahead
#         # of their current position
#         while j >= 0 and key < arr[j]:
#             arr[j + 1] = arr[j]
#             j -= 1
#         arr[j + 1] = key

# # A utility function to print array of size n
# def printArray(arr):
#     for i in range(len(arr)):
#         print(arr[i], end=" ")
#     print()

# # Driver method
# if __name__ == "__main__":
#     arr = [12, 11, 13, 5, 6]
#     insertionSort(arr)
#     printArray(arr)

#     # This code is contributed by Hritik Shah.

# selection sort
def selectionSort(array):
    for i in range(0, len(array) - 1): # batasnya sampai len(array) - 1 karena pada array terakhir tidak perlu disorting lagi
        cur_min_idx = i
        for j in range(i + 1, len(array)):
            if array[j] < array[cur_min_idx]:
                cur_min_idx = j

        array[i], array[cur_min_idx] = array[cur_min_idx], array[i] # swap

array = [12, 334, 43, 55, 7]
selectionSort(array)
print("pengurutan data dengan selection sort")
print(array)

