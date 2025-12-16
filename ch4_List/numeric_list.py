'''
for i in range(1, 5): # always write n+1 to include n
    print(i)
'''

'''
# make list of numbers
numbers = list(range(1,6))
print(numbers)
'''

'''
numbers = list(range(2, 11, 2)) # (start, stop, step)
print(numbers)
'''

'''
# squares of first 10 numbers
squares = []
for i in range(1, 11):
    squares.append(i**2)
    #print(squares) incorrectrly placed
    
print(squares)
print("minimum:", min(squares))
print("maximum:", max(squares))
print("Sum:", sum(squares))
'''

'''
# list comprehension
squares  = [i**2 for i in range(1,11)]
print(squares)
'''