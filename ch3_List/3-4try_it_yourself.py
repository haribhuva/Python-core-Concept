'''
3-4. Guest List: If you could invite anyone, living or deceased, to dinner, who
would you invite? Make a list that includes at least three people you’d like to
invite to dinner. Then use your list to print a message to each person, inviting
them to dinner.
'''

list = ["Viren", "Ankesh", "Jainam"]
print(f"Dear {list[0]}, I would like to invite you on dinner.")
print(f"Dear {list[1]}, I would like to invite you on dinner.")
print(f"Dear {list[2]}, I would like to invite you on dinner.")

'''
3-5. Changing Guest List: You just heard that one of your guests can’t make the
dinner, so you need to send out a new set of invitations. You’ll have to think of
someone else to invite.
•Start with your program from Exercise 3-4. Add a print() call at the end of
your program, stating the name of the guest who can’t make it.
•Modify your list, replacing the name of the guest who can’t make it with the
name of the new person you are inviting.
•Print a second set of invitation messages, one for each person who is still in
your list.
'''

print(f"\nUnfortunatly, {list[2]}, can't come for the dinner.")
list[2] = "Ruhin"
print(f"Dear {list[0]}, I would like to invite you on dinner.")
print(f"Dear {list[1]}, I would like to invite you on dinner.")
print(f"Dear {list[2]}, I would like to invite you on dinner.")

'''
3-6. More Guests: You just found a bigger dinner table, so now more space is
available. Think of three more guests to invite to dinner.
•Start with your program from Exercise 3-4 or 3-5. Add a print() call to the
end of your program, informing people that you found a bigger table.
•Use insert() to add one new guest to the beginning of your list.
•Use insert() to add one new guest to the middle of your list.
•Use append() to add one new guest to the end of your list.
•Print a new set of invitation messages, one for each person in your list.
'''

print("\nGood news! We found a bigger dinner table.")
list.insert(0, "Ronak")
list.insert(2, "Dhrumil")
list.append("Khushi")
print(f"Dear {list[0]}, I would like to invite you on dinner.")
print(f"Dear {list[1]}, I would like to invite you on dinner.")
print(f"Dear {list[2]}, I would like to invite you on dinner.")
print(f"Dear {list[3]}, I would like to invite you on dinner.")
print(f"Dear {list[4]}, I would like to invite you on dinner.")
print(f"Dear {list[5]}, I would like to invite you on dinner.")


print("\nnew dinner table won’t arrive in time for the dinner, and I have space only for two people.")
print(f"Sorry to inform {list[1], list[2], list[4]} and {list[5]} that you can't come for dinner.")
print(f"Dear {list[0]} and {list[3]}, you are still invited for dinner.")
list.pop(1)
list.pop(2)
del list[-2]
del list[-1]
print(f"\nFinal guest list: {list}, and total number of guests is: {len(list)}")