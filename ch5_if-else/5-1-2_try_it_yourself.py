'''
5-1. Conditional Tests: Write a series of conditional tests. Print a statement
describing each test and your prediction for the results of each test. Your code
should look something like this:
car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')
print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')
•Look closely at your results, and make sure you understand why each line
evaluates to True or False.
•Create at least 10 tests. Have at least 5 tests evaluate to True and another
5 tests evaluate to False.

note: this is for basic understanding of conditional tests in Python. so if you want to do
you should do it in a simple way.
'''

'''
5-2. More Conditional Tests: You don’t have to limit the number of tests you cre-
ate to 10. If you want to try more comparisons, write more tests and add them
to conditional_tests.py. Have at least one True and one False result for each of
the following:
•Tests for equality and inequality with strings
•Tests using the lower() method
•Numerical tests involving equality and inequality, greater than and less
than, greater than or equal to, and less than or equal to
•Tests using the and keyword and the or keyword
•Test whether an item is in a list
•Test whether an item is not in a list
'''

list = ['apple', 'banana', 'cherry', 1, 2, 3]
fruit = 'banana'
number = 2
print(f"test for apple is avalible in list or not: {'apple' in list}")
print(f"test for grap is not avalible in list or not: {'grape' in list}")
print(f"test for 4 is not avalible in list or not: {4 in list}")
print(f"test for 3 is not avalible in list or not: {3 in list}")
print(f"test for fruit variable is equal to banana: {fruit == 'banana'}")
print(f"test for fruit variable is not equal to orange: {fruit != 'orange'}")
print(f"test for fruit variable is equal to banana: {fruit != 'banana'}")
print(number > -1)
#print(2 in number) # not working because number is not iterable
print(number >= 2)
print(number < 5 and fruit == 'banana')
print(number > 5 or fruit == 'banana')
print(fruit.lower() == 'BANANA'.lower())
print(fruit.lower() == 'ORANGE'.lower())