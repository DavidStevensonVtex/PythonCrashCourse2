alien_0 = { 'color': 'green',  'points': 5 }
alien_1 = { 'color': 'yellow', 'points': 10 }
alien_2 = { 'color': 'red',    'points': 15 }

aliens = [ alien_0, alien_1, alien_2 ]

for alien in aliens:
    print(alien)

print("\n")
aliens = []
aliens.append(alien_0)
aliens.append(alien_1)
aliens.append(alien_2)

for alien in aliens:
    print(alien)

# {'color': 'green', 'points': 5}
# {'color': 'yellow', 'points': 10}
# {'color': 'red', 'points': 15}


# {'color': 'green', 'points': 5}
# {'color': 'yellow', 'points': 10}
# {'color': 'red', 'points': 15}