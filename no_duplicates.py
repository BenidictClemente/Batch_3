numbers = []

for _ in range(10):
    numbers.append(int(input("Enter a number: ")))

for num in numbers:
    if numbers.count(num) == 1:
        print(num)
