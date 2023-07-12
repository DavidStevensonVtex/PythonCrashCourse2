alien_0 = { 'x_position': 0, 'y_position': 25, 'speed': 'medium' }
print(f"Original x position: {alien_0['x_position']}  Speed: {alien_0['speed']}")

# Move the alien to the right.
# Determine how far to move the alien based on its current speed.

if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    # This must be a fast alien.
    x_increment = 3

# The new position is the old position plus the increment.
alien_0['x_position'] = alien_0['x_position'] + x_increment
print(f"New x position: {alien_0['x_position']}")

# Original x position: 0  Speed: medium
# New x position: 2