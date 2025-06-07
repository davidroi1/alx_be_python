def perform_operation(num1, num2, operation):
    if operation == 'divide':
        if num2 == 0:
            raise ZeroDivisionError("error: impossible to divide number by zero")
        return num1 / num2
    elif operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2