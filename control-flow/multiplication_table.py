number = int(input("Enter a number to see its multiplication table:"))

for num in range(1, number + 1):
    print(f'{number} x {num} = {number * num}')