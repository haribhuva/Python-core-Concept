'''
4-13. Buffet: A buffet-style restaurant offers only five basic foods. Think of five
simple foods, and store them in a tuple.
•Use a for loop to print each food the restaurant offers.
•Try to modify one of the items, and make sure that Python rejects the
change.
•The restaurant changes its menu, replacing two of the items with different
foods. Add a line that rewrites the tuple, and then use a for loop to print
each of the items on the revised menu.
'''
buffet_foods = ('salad', 'soup', 'bread', 'pasta', 'dessert')
for food in buffet_foods:
    print(f"This all are buffet food items: {food}")
# buffet_foods[0] = 'steak'  # This will raise an error because tuples are immutable
buffet_foods = ('steak', 'soup', 'bread', 'rice', 'dessert')
#print("\nRevised menu:")
#reversed = reversed(buffet_foods)
#print(tuple(reversed))
for food in reversed(buffet_foods):
    print(f"This all are reversed buffet food items: {food}")