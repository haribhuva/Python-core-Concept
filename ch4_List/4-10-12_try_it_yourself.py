'''
4-10. Slices: Using one of the programs you wrote in this chapter, add several
lines to the end of the program that do the following:
•Print the message The first three items in the list are:. Then use a slice to
print the first three items from that program’s list.
•Print the message Three items from the middle of the list are:. Then use a
slice to print three items from the middle of the list.
•Print the message The last three items in the list are:. Then use a slice to
print the last three items in the list.

list = ['apple', 'banana', 'cherry', 'date', 'fig', 'grape', 'kiwi']
print("Original list:", list)
print("The first three items in the list are:", list[:3])
print("Three items from the middle of the list are:", list[2:5])
print("The last three items in the list are:", list[-3:])
'''

'''
4-11. My Pizzas, Your Pizzas: Start with your program from Exercise 4-1 (page 56).
Make a copy of the list of pizzas, and call it friend_pizzas. Then, do the
following:
•Add a new pizza to the original list.
•Add a different pizza to the list friend_pizzas.
•Prove that you have two separate lists. Print the message My favorite piz-
zas are:, and then use a for loop to print the first list. Print the message My
friend’s favorite pizzas are:, and then use a for loop to print the second list.
Make sure each new pizza is stored in the appropriate list.

my_pizzas = ["Farm willa", "seven cheezy", "sweet corn"]

copy_my_pizzas = my_pizzas[:]
my_pizzas.append("peri peri")

friend_pizzas = my_pizzas[:]
friend_pizzas.append("veggie delight")

for pizza in my_pizzas:
    print(f"my fevirote pizzas are: {pizza}")
for pizza in friend_pizzas:
    print(f"my friends fevirote pizzas are: {pizza}")
'''

'''
4-12. More Loops: All versions of foods.py in this section have avoided using
for loops when printing, to save space. Choose a version of foods.py, and
write two for loops to print each list of foods.

foods = ['burger', 'pizza', 'pasta', 'sushi', 'salad']
for food in foods:
    print(f"I like {food}!")

print("\nI really love food!")
'''