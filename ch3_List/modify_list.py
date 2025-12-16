"""
list = ["2", "3", "4", "5", "6"]
print("Original list:", list)
list[0] = "1"
print("Replace value with 1 in list with list[0]:", list)
list.append("7")
print("List after append:", list)
del list[5]
print("List after deleting index 5:", list)
"""

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
popped_motorcycle = motorcycles.pop(1)
print(motorcycles)
print(popped_motorcycle)