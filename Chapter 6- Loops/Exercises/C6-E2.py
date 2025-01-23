
while True:
    age = input("Enter your age (or 'quit' to exit): ")

    if age.lower() == 'quit':
        print("Thank you for visiting!")
        break

    try:
        age = int(age)
        if age < 3:
            price = "Free"
        elif 3 <= age <= 12:
            price = 10
        else:
            price = 15

        print(f"The ticket price is: ${price}")
    except ValueError:
        print("Please enter a valid number for your age.")
