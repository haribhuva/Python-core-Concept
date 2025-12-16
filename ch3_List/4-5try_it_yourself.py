list = ["Sanfrancisco", "Bali", "Kyoto", "Singapore", "Iceland"]
print("Original list:", list)
print("Sorted list: ",sorted(list))
print("printing in reverse order using slicing: ", list[::-1])
list.reverse()
print("List in reverse order using reverse():", list)
list.reverse()
print("List after reversing again to original:", list)