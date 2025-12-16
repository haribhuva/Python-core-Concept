'''
5-8. Hello Admin: Make a list of five or more usernames, including the name
'admin'. Imagine you are writing code that will print a greeting to each user
after they log in to a website. Loop through the list, and print a greeting to
each user.
•If the username is 'admin', print a special greeting, such as Hello admin,
would you like to see a status report?
•Otherwise, print a generic greeting, such as Hello Jaden, thank you for
logging in again.

admins = ['admin', 'user1', 'user2', 'user3', 'user4']
name = input('Enter your username: ')
if name in admins:
    if name == 'admin':
        print('Hello admin, would you like to see a status report?')
    else:
        print(f'Hello {name}, thank you for logging in again.')
else:
    print('Username not found. Please sign up.')
'''

'''
5-9. No Users: Add an if test to hello_admin.py to make sure the list of users is
not empty.
•If the list is empty, print the message We need to find some users!
•Remove all of the usernames from your list, and make sure the correct mes-
sage is printed.

no_users = []
users = ['admin', 'user1', 'user2', 'user3', 'user4']
entry = input('Would you like to see the user list? (yes/no): ')
if entry == 'yes':
    for user in users:
        if user == 'admin':
            print('hello admin would you like to see a status report?')
        else:
            print(f'hello {user}, thak you for logging in again.')
else:
    print('We need to find some users!')
'''

'''
5-10. Checking Usernames: Do the following to create a program that simulates
how websites ensure that everyone has a unique username.
•Make a list of five or more usernames called current_users.
•Make another list of five usernames called new_users. Make sure one or
two of the new usernames are also in the current_users list.
•Loop through the new_users list to see if each new username has already
been used. If it has, print a message that the person will need to enter a
new username. If a username has not been used, print a message saying
that the username is available.
•Make sure your comparison is case insensitive. If 'John' has been used,
'JOHN' should not be accepted. (To do this, you’ll need to make a copy of
current_users containing the lowercase versions of all existing users.)

current_users = ['admin', 'user1', 'user2', 'user3', 'user4']
new_users = ['User1', 'newuser', 'Admin', 'guest', 'user5']

current_users = [user.lower() for user in current_users]
new_users = [user.lower() for user in new_users]

for i in new_users:
    if i in current_users:
        print(f'the username {i} is already taken. select a new username.')
    else:
        print(f'the username {i} is available.')
'''

'''
5-11. Ordinal Numbers: Ordinal numbers indicate their position in a list, such as
1st or 2nd. Most ordinal numbers end in th, except 1, 2, and 3.
•Store the numbers 1 through 9 in a list.
•Loop through the list.
•Use an if- elif- else chain inside the loop to print the proper ordinal ending
for each number. Your output should read "1st 2nd 3rd 4th 5th 6th 7th
8th 9th", and each result should be on a separate line.

number = list(range(1, 10))

for i in number:
    if i == 1:
        print(f'{i}st')
    elif i == 2:
        print(f'{i}nd')
    elif i == 3:
        print(f'{i}rd')
    else:
        print(f'{i}th')
'''

'''
5-12. Styling if Statements: Review the programs you wrote in this chapter, and
make sure you styled your conditional tests appropriately.
'''

'''
5-13. Your Ideas: At this point, you’re a more capable programmer than you
were when you started this book. Now that you have a better sense of how
real-world situations are modeled in programs, you might be thinking of some
problems you could solve with your own programs. Record any new ideas you
have about problems you might want to solve as your programming skills con-
tinue to improve. Consider games you might want to write, datasets you might
want to explore, and web applications you’d like to create.
'''