'''6-1. Person: Use a dictionary to store information about a person you know.
Store their first name, last name, age, and the city in which they live. You
should have keys such as first_name, last_name, age, and city. Print each piece
of information stored in your dictionary.

person = {
    'first_name': 'ronak',
    'last_name': 'kaila',
    'age': 28,
    'city': 'morbi'
}

for i, j in person.items():
    print(f'{i}: {j}')
'''

'''
6-2. Favorite Numbers: Use a dictionary to store people’s favorite numbers.
Think of five names, and use them as keys in your dictionary. Think of a favorite
number for each person, and store each as a value in your dictionary. Print
each person’s name and their favorite number. For even more fun, poll a few
friends and get some actual data for your program.

fevirote_numbers = {
    'ronak': 22,
    'viren': 19,
    'dharmik': 17,
    'chirag': 11,
    'hari': 31
}

for i, j in fevirote_numbers.items():
    print(f'Name of the prson is, {i} and his favorite number is {j}')
'''

'''
6-3. Glossary: A Python dictionary can be used to model an actual dictionary.
However, to avoid confusion, let’s call it a glossary.
•Think of five programming words you’ve learned about in the previous
chapters. Use these words as the keys in your glossary, and store their
meanings as values.
•Print each word and its meaning as neatly formatted output. You might
print the word followed by a colon and then its meaning, or print the word
on one line and then print its meaning indented on a second line. Use the
newline character (\n) to insert a blank line between each word-meaning
pair in your output.

glossary = {
    'integer': 'A whole number, positive or negative, without decimals, of unlimited length.',
    'float': 'A number, positive or negative, containing one or more decimals.',
    'string': 'A series of characters enclosed in single or double quotes.',
    'boolean': 'A data type that can only have one of two values: True or False.',
    'character': 'A single letter, number, symbol, or space.'
}

for i, j in glossary.items():
    print(f'* meaning of the "{i}" is:\n -> {j}')
'''

'''
6-4. Glossary 2: Now that you know how to loop through a dictionary, clean
up the code from Exercise 6-3 (page 99) by replacing your series of print()
calls with a loop that runs through the dictionary’s keys and values. When
you’re sure that your loop works, add five more Python terms to your glossary.
When you run your program again, these new words and meanings should
automatically be included in the output.

glossary = {
    'integer': 'A whole number, positive or negative, without decimals, of unlimited length.',
    'float': 'A number, positive or negative, containing one or more decimals.',
    'string': 'A series of characters enclosed in single or double quotes.',
    'boolean': 'A data type that can only have one of two values: True or False.',
    'character': 'A single letter, number, symbol, or space.'  
}

del glossary['character']
del glossary['boolean']

glossary['list'] = 'A collection of items in a particular order.'
glossary['tuple'] = 'An immutable collection of items in a particular order.'
glossary['dictionary'] = 'A collection of key-value pairs.'

for i, j in glossary.items():
    print(f'Updated glossary details\n* meaning of the "{i}" is:\n -> {j}')

#Solution note:
# also we should use glossary.update() method but is is just add the content
# not remove the existing one.
'''

'''
6-5. Rivers: Make a dictionary containing three major rivers and the country
each river runs through. One key-value pair might be 'nile': 'egypt'.
•Use a loop to print a sentence about each river, such as The Nile runs
through Egypt.
•Use a loop to print the name of each river included in the dictionary.
•Use a loop to print the name of each country included in the dictionary.

rivers = {
    'nile': 'egypt',
    'ganga': 'india',
    'amazon': 'brazil'
}

for i, j in rivers.items():
    print(f' The {i} runs through {j}.')
'''

'''
6-6. Polling: Use the code in favorite_languages.py (page 96).
•Make a list of people who should take the favorite languages poll. Include
some names that are already in the dictionary and some that are not.
•Loop through the list of people who should take the poll. If they have
already taken the poll, print a message thanking them for responding.
If they have not yet taken the poll, print a message inviting them to take
the poll.

people = ['jen', 'sarah', 'edward', 'phil', 'ronak', 'viren']
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
}
for person in people:
    if person in favorite_languages:
        print(f'Thank you {person.title()} for responding to the poll.')
    else:
        print(f'{person.title()}, please take the favorite languages poll.')
'''

'''
6-7. People: Start with the program you wrote for Exercise 6-1 (page 98). Make
two new dictionaries representing different people, and store all three dictionar-
ies in a list called people. Loop through your list of people. As you loop through
the list, print everything you know about each person.
6-8. Pets: Make several dictionaries, where each dictionary represents a differ-
ent pet. In each dictionary, include the kind of animal and the owner’s name.
Store these dictionaries in a list called pets. Next, loop through your list and as
you do, print everything you know about each pet.
6-9. Favorite Places: Make a dictionary called favorite_places. Think of three
names to use as keys in the dictionary, and store one to three favorite places for
each person. To make this exercise a bit more interesting, ask some friends to
name a few of their favorite places. Loop through the dictionary, and print each
person’s name and their favorite places.
6-10. Favorite Numbers: Modify your program from Exercise 6-2 (page 98) so
each person can have more than one favorite number. Then print each person’s
name along with their favorite numbers.
6-11. Cities: Make a dictionary called cities. Use the names of three cities as
keys in your dictionary. Create a dictionary of information about each city and
include the country that the city is in, its approximate population, and one fact
about that city. The keys for each city’s dictionary should be something like
country, population, and fact. Print the name of each city and all of the infor-
mation you have stored about it.
6-12. Extensions: We’re now working with examples that are complex enough
that they can be extended in any number of ways. Use one of the example pro-
grams from this chapter, and extend it by adding new keys and values, chang-
ing the context of the program, or improving the formatting of the output.
'''