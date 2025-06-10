FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5


def convert_to_celsius(fahrenheit):
    #Convert Fahrenheit to Celsius.
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    #Convert Celsius to Fahrenheit.
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

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
        print("Invalid temperature. Please enter a numeric value.")


if __name__ == "__main__":
    main()




"""FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
  temp = (fahrenheit - 32 ) * FAHRENHEIT_TO_CELSIUS_FACTOR
  print(f'{fahrenheit}\N{DEGREE SIGN}F is {temp}\N{DEGREE SIGN}C')

def convert_to_fahrenheit(celsius):
  temp = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
  print(f'{celsius}\N{DEGREE SIGN}C is {temp}\N{DEGREE SIGN}F')


try:
  temp = float(input('Enter the temperature to convert:'))
  unit = (input('Is this temperature in Celsius or Fahrenheit? (C/F): '))

  if unit.upper() == 'C':
    convert_to_fahrenheit(temp)
  elif unit.upper() == 'F':
    convert_to_celsius(temp)
  else:
    exit(1)
except ValueError:
  print('Invalid temperature. Please enter a numeric value.')"""