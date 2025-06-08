FAHRENHEIT_TO_CELSIUS_RATIO = 5 / 9
CELSIUS_TO_FAHRENHEIT_RATIO = 9 / 5

def convert_to_celsius(fahrenheit):
    #Convert Fahrenheit to Celsius.
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_RATIO

def convert_to_fahrenheit(celsius):
    #Convert Celsius to Fahrenheit.
    return (celsius * CELSIUS_TO_FAHRENHEIT_RATIO) + 32

def main():
    try:
        temperature = float(input('Enter the temperature to convert: '))
        choice = input('Is this temperature in Celsius or Fahrenheit? (C/F): ').upper()

        if choice == 'F':
            converted = convert_to_celsius(temperature)
            print(f'{temperature}°F is {converted}°C')  # Fixed message
        elif choice == 'C':
            converted = convert_to_fahrenheit(temperature)
            print(f'{temperature}°C is {converted}°F')  # Fixed message
        else:
            print('Invalid choice. Please enter "C" or "F".')

    except ValueError:
        print('Error: Temperature must be a number.')


if __name__ == "__main__":
    main()