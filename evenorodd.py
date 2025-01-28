numbers=input("enter numbers:").split()

even_numbers=[int(num)for num in numbers if int(num)%2==0]
odd_numbers=[int(num) for num in numbers if int(num)%2!=0]

print("even numbers are: ",even_numbers)
print("odd numbers are: ",odd_numbers)