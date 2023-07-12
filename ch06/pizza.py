# Store information about a pizza being ordered.
pizza = {
    'crust': 'thick',
    'toppings': [ 'mushrooms', 'extra cheese' ]
}
# print (pizza)

print(f"You ordered a {pizza['crust']}-crust pizza with the following toppings: ")
for topping in pizza['toppings']:
    print(f"\t{topping}")

# You ordered a thick-crust pizza with the following toppings: 
#         mushrooms
#         extra cheese