temp=float(input("Enter the temperature value: "))
scale=input("enter the scale (C for celsius, F for Farenheit, K for Kelvin): ").upper()

if scale=='C':
    farenheit=(temp*9/5)+32
    kelvin=temp+273.15
    print(f"{temp}C={farenheit}F")
    print(f"{temp}C={kelvin}K")
elif scale=='F':
    celsius=(temp-32)*5/9
    kelvin=celsius+273.15
    print(f"{temp}F={celsius}C")
    print(f"{temp}F={kelvin}K")
elif scale=='K':
    celsius=temp-273.15
    farenheit=(temp*9/5)+32
    print(f"{temp}K={celsius}C")
    print(f"{temp}K={farenheit}F")
else:
    print("invalid")