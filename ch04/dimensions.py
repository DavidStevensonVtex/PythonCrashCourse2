# an immutable list is called a tuple.

dimensions = (200,50)
print(dimensions[0])
print(dimensions[1])
print(dimensions)

for dimension in dimensions:
    print(dimension)

# 200
# 50
# (200, 50)

# If you want to define a tuple with one element:

my_t = (3,)
print(my_t)
# (3,)