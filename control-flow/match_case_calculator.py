num_1 = int(input("Enter the first number:"))
num_2 = int(input("Enter the second number:"))
operator = input("Choose the operation (+, -, *, /):")


if operator == '+':
    print(f'The result is {num_1 + num_2}.')
elif operator == '-':
    print(f'The result is {num_1 - num_2}.')
elif operator == '*':
    print(f'The result is {num_1 * num_2}.')
elif operator == '/':
    if num_2 == 0:
        print("Cannot divide by zero.")
    else:
        print(f'The result is {num_1 / num_2}.')