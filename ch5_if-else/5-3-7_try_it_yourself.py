'''
5-3. Alien Colors #1: Imagine an alien was just shot down in a game. Create a
variable called alien_color and assign it a value of 'green', 'yellow', or 'red'.
•Write an if statement to test whether the alien’s color is green. If it is, print
a message that the player just earned 5 points.
•Write one version of this program that passes the if test and another that
fails. (The version that fails will have no output.)

alien_color = 'green'
if alien_color == "green":
    print("player earned 5 points.")
if alien_color == "yellow":
    print("player earned 5 points.")
'''

'''
5-4. Alien Colors #2: Choose a color for an alien as you did in Exercise 5-3,
and write an if- else chain.
•If the alien’s color is green, print a statement that the player just earned 5
points for shooting the alien.
•If the alien’s color isn’t green, print a statement that the player just earned
10 points.
•Write one version of this program that runs the if block and another that
runs the else block.

alien_colur = input("enter the alien color('green/yellow/red'): ")
if alien_colur == 'green' or alien_colur == 'yellow' or alien_colur == 'red':
    pass
    if alien_colur == 'green':
        print('player just earned 5 points for shooting the alien.')
    elif alien_colur != 'green':
        print('player just earn 10 points.')
    else:
        print('no points earned.')
else:
    print('invalid color input.')
'''

'''
5-5. Alien Colors #3: Turn your if- else chain from Exercise 5-4 into an if- elif-
else chain.
•If the alien is green, print a message that the player earned 5 points.
•If the alien is yellow, print a message that the player earned 10 points.
•If the alien is red, print a message that the player earned 15 points.
•Write three versions of this program, making sure each message is printed
for the appropriate color alien.

alien_colour = input("enter the alien color('green/yellow/red'): ")
if alien_colour == 'green' or alien_colour == 'yellow' or alien_colour == 'red':
    pass
    if alien_colour == 'green':
        print('player earn 5 points for shooting an alien.')
    elif alien_colour == 'yellow':
        print('player earned 10 points.')
    else:
        print('player earned 15 points for the red colour.')
else:
    print('Enter valid input.')
'''

'''
5-6. Stages of Life: Write an if- elif- else chain that determines a person’s stage
of life. Set a value for the variable age, and then:
•If the person is less than 2 years old, print a message that the person is
a baby.
•If the person is at least 2 years old but less than 4, print a message that the
person is a toddler.
•If the person is at least 4 years old but less than 13, print a message that
the person is a kid.
•If the person is at least 13 years old but less than 20, print a message that
the person is a teenager.
•If the person is at least 20 years old but less than 65, print a message that
the person is an adult.
•If the person is age 65 or older, print a message that the person is an elder.


age = int(input('Enter number of age here: '))
if age < 2:
    print('the person is baby.')
elif age >= 2 and age < 4:
    print('person is toddler.')
elif 4 >= age < 13:
    print('person is kid.')
elif age >=13 and age <20:
    print('person is teenager.')
elif age >=20 and age <65:
    print('person is adult.')
else:
    print('person is elder.')
'''

'''
5-7. Favorite Fruit: Make a list of your favorite fruits, and then write a series of
independent if statements that check for certain fruits in your list.
•Make a list of your three favorite fruits and call it favorite_fruits.
•Write five if statements. Each should check whether a certain kind of fruit
is in your list. If the fruit is in your list, the if block should print a statement,
such as You really like bananas!
'''

fevorite_fruits = ['mango', 'dragon fruite', 'watermelon']
user = input('Enter your fevorite fruit: ')

if user in fevorite_fruits:
    pass
    if user == 'mago':
        print('user really like mango!')
    elif user == 'dragon fruite':
        print('user really like dragon fruite!')
    else:
        print('user really like watermelon!')
else:
    print(f'The fruit {user} is not in the list.')