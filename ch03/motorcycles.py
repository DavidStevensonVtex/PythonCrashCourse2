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