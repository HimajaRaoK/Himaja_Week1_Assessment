num = int(input("Enter a number: "))  #user input

if num < 0:
    print("Error: Factorial doesnt exist for negative numbers.") #for negative numbers
else:
    factorial = 1
    for i in range(1, num + 1):    
        factorial *= i            

    print(f"The factorial of {num} is: {factorial}") 
