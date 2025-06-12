num_1 = int(input("Enter the first number:"))
num_2 = int(input("Enter the second number:"))
match_operation = input("Choose the operation (+, -, *, /):")


if match_operation == '+':
    print(f'The result is {num_1 + num_2}.')
elif match_operation == '-':
    print(f'The result is {num_1 - num_2}.')
elif match_operation == '*':
    print(f'The result is {num_1 * num_2}.')
elif match_operation == '/':
    if num_2 == 0:
        print("Cannot divide by zero.")
    else:
        print(f'The result is {num_1 / num_2}.')
