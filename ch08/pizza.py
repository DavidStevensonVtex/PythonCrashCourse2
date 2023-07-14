def make_pizza(*toppings):
    """Summarize the pizza we are about to make."""
    print("\nMaking a piza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")

make_pizza('pepperoni')
make_pizza('mushrooms', 'green_peppers', 'extra_cheese')