# Function to convert Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# Function to convert Celsius to Kelvin
def celsius_to_kelvin(celsius):
    return celsius + 273.15

# Function to convert Fahrenheit to Celsius
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

# Function to convert Fahrenheit to Kelvin
def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit - 32) * 5/9 + 273.15

# Function to convert Kelvin to Celsius
def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

# Function to convert Kelvin to Fahrenheit
def kelvin_to_fahrenheit(kelvin):
    return (kelvin - 273.15) * 9/5 + 32

# Function to convert the temperature based on the input unit
def convert_temperature(value, unit):
    if unit == 'C':
        fahrenheit = celsius_to_fahrenheit(value)
        kelvin = celsius_to_kelvin(value)
        print(f"\n{value}°C is:")
        print(f" {fahrenheit}°F")
        print(f" {kelvin}K")
    elif unit == 'F':
        celsius = fahrenheit_to_celsius(value)
        kelvin = fahrenheit_to_kelvin(value)
        print(f"\n{value}°F is:")
        print(f" {celsius}°C")
        print(f" {kelvin}K")
    elif unit == 'K':
        celsius = kelvin_to_celsius(value)
        fahrenheit = kelvin_to_fahrenheit(value)
        print(f"\n{value}K is:")
        print(f" {celsius}°C")
        print(f" {fahrenheit}°F")
    else:
        print("Invalid unit of temperature. Please enter 'C' for Celsius, 'F' for Fahrenheit, or 'K' for Kelvin.")

# Main function to run the program
def main():
    try:
        # Asking the user to input the temperature value
        value = float(input("Enter the temperature value: "))
        # Asking the user to input the unit (C, F, or K)
        unit = input("Enter the unit (C for Celsius, F for Fahrenheit, K for Kelvin): ").upper()
        # Calling the convert_temperature function to perform the conversion
        convert_temperature(value, unit)
    except ValueError:
        # Error handling for invalid input
        print("Please enter a valid numeric value for the temperature.")

# Running the main function
if __name__ == "__main__":
    main()