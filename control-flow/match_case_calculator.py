num_1 = int(input("Enter the first number:"))
num_2 = int(input("Enter the second number:"))
match_operation = input("Choose the operation (+, -, *, /):")


match match_operation:
    case '+': 
        print(f'The result is {num_1 + num_2}.')
    case '*': 
        print(f'The result is {num_1 * num_2}.')
    case '/': 
        if num_2 == 0:
            print("Cannot divide by zero.")
        else:
            print(f'The result is {num_1 / num_2}.')
    case _:
        print('Cannot find this instruction')
