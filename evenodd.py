# Taking user input for a list of numbers
numbers = input("Enter numbers: ").split()   #split should be used or it will give error as it doesnt know that they are seperate values

# to create seperate lists for even and odd, and also formula to check 
even_numbers = [int(num) for num in numbers if int(num) % 2 == 0]
odd_numbers = [int(num) for num in numbers if int(num) % 2 != 0]

# printing the output
print("Even numbers:", even_numbers)
print("Odd numbers:", odd_numbers)
