from random import randint, choice
print(f"randint(1,6) {randint(1,6)}")

players = [ 'charles', 'martina', 'michael', 'florence', 'eli' ]
first_up = choice(players)
print(f"first_up: {first_up}")

# randint(1,6) 3
# first_up: charles