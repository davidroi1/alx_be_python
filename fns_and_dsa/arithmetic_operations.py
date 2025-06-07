def perform_operation(num1, num2, operation):
    if operation == 'divide':
        try:
            result = num1 / num2
        except ZeroDivisionError:
            return "error: impossible to divide number by zero"
        else:
            return result
    elif operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2