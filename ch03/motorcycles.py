motorcycles = [ 'honda', 'yamaha', 'suzuki' ]
print(motorcycles)

motorcycles[0] = 'ducati'
print(motorcycles)

# ['honda', 'yamaha', 'suzuki']
# ['ducati', 'yamaha', 'suzuki']

motorcycles = [ 'honda', 'yamaha', 'suzuki' ]
motorcycles.append('ducati')
print(motorcycles)
# ['honda', 'yamaha', 'suzuki', 'ducati']

motorcycles = []
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)
# ['honda', 'yamaha', 'suzuki']

# Inserting Elements into a list
motorcycles = [ 'honda', 'yamaha', 'suzuki' ]
motorcycles.insert(0, 'ducati')
print(motorcycles)
['ducati', 'honda', 'yamaha', 'suzuki']

# Removing an Item using the del Statement
motorcycles = [ 'honda', 'yamaha', 'suzuki' ]
print(motorcycles)
del motorcycles[0]
print(motorcycles)
# ['honda', 'yamaha', 'suzuki']
# ['yamaha', 'suzuki']

# Removing an Item Using the pop() Method
motorcycles = [ 'honda', 'yamaha', 'suzuki' ]
print(motorcycles)
popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)
# ['honda', 'yamaha', 'suzuki']
# ['honda', 'yamaha']
# suzuki

motorcycles = [ 'honda', 'yamaha', 'suzuki' ]
last_owned = motorcycles.pop()
print(f"The last motorcycle I owned was a {last_owned.title()}")
# The last motorcycle I owned was a Suzuki

# Popping Items from any Position in a List
motorcycles = [ 'honda', 'yamaha', 'suzuki' ]
first_owned = motorcycles.pop(0)
print(f"The first motorcycle I owned was a {first_owned.title()}")
# The first motorcycle I owned was a Honda