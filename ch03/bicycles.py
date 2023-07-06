bicycles = [ 'trek', 'cannondale', 'redline', 'specialized' ] ;
print(bicycles)
# ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[0])
# trek
print(bicycles[0].title())
# Trek

# Index positions start at 0, not 1
print(bicycles[1])
print(bicycles[3])
# cannondale
# specialized

# Print last element of the list using index -1
print(bicycles[-1])
# specialized

# Using Individual Values from a List
message = f"My first bicycle was a {bicycles[0].title()}"
print(message)
# My first bicycle was a Trek