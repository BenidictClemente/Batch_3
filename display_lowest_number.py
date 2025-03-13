lowest_number = None
while True:
    user_input = input("Enter a number: ")
    try:
        number = int(user_input)
    except ValueError:
        print("Invalid input!")
        break

    if lowest_number is None or number < lowest_number:
        lowest_number = number

print(lowest_number)
