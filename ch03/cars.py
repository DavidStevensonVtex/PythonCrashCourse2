# Sorting a List Permanently with the sort() Method
cars = [ 'bmw', 'audi', 'toyota', 'subaru' ]
cars.sort()
print(cars)
# ['audi', 'bmw', 'subaru', 'toyota']

# Sorting a List Permanently in Reverse Order
cars = [ 'bmw', 'audi', 'toyota', 'subaru' ]
cars.sort(reverse=True)
print(cars)
# ['toyota', 'subaru', 'bmw', 'audi']

# Sorting a List Temporarily with the sorted() Function
cars = [ 'bmw', 'audi', 'toyota', 'subaru' ]
print("\nHere is the original list")
print(cars)

print("\nHere is the sorted list:")
print(sorted(cars))

print("\nHere is the original list again:")
print(cars)

# Here is the original list
# ['bmw', 'audi', 'toyota', 'subaru']

# Here is the sorted list:
# ['audi', 'bmw', 'subaru', 'toyota']

# Here is the original list again:
# ['bmw', 'audi', 'toyota', 'subaru']