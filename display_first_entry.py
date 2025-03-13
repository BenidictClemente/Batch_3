numbers = []
unique_numbers = []

for _ in range(10):
    number = int(input("Enter a number: "))
    numbers.append(number)

for num in numbers:
    if num not in unique_numbers:
        unique_numbers.append(num)
        print(num)
