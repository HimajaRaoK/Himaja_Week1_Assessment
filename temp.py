# Taking user input for temperature and scale
temp = float(input("Enter the temperature value: "))
scale = input("Enter the scale (C for Celsius, F for Fahrenheit, K for Kelvin): ").upper()

#for each temp- conversions
if scale == 'C':
    fahrenheit = (temp * 9/5) + 32
    kelvin = temp + 273.15
    print(f"{temp}°C = {fahrenheit}°F")
    print(f"{temp}°C = {kelvin}K")
elif scale == 'F':
    celsius = (temp - 32) * 5/9
    kelvin = celsius + 273.15
    print(f"{temp}°F = {celsius}°C")
    print(f"{temp}°F = {kelvin}K")
elif scale == 'K':
    celsius = temp - 273.15
    fahrenheit = (celsius * 9/5) + 32
    print(f"{temp}K = {celsius}°C")
    print(f"{temp}K = {fahrenheit}°F")
else:
    print("Invalid")
