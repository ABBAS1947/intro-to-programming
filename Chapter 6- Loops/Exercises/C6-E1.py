
while True:
    topping = input("Enter a pizza topping (or 'quit' to stop): ").lower()

    if topping == 'quit':
        print("Thanks for your order!")
        break
    else:
        print(f"Adding {topping} to your pizza.")
