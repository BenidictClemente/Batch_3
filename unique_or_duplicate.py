numbers = []

while True:
    user_input = input("Enter a number: ")
    
    try:
        number = int(user_input)
    except ValueError:
        print("Invalid input! Exiting program.")
        break
    
    if number in numbers:
        print("Duplicate")
    else:
        print("Unique")
    
    numbers.append(number)
