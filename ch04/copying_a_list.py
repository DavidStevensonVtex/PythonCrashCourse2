my_foods = [ 'pizza', 'falafel', 'carrot cake' ]
friend_foods = my_foods     # This doesn't work. A list reference is copied, and a new list is not made.
my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)

# My favorite foods are:
# ['pizza', 'falafel', 'carrot cake', 'cannoli']

# My friend's favorite foods are:
# ['pizza', 'falafel', 'carrot cake', 'ice cream']