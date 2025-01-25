def is_prime(num):    #formula to check if the number is prime or not
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def primes_between(a, b):      #range - to print only prime numbers in that range 
    return [num for num in range(a, b + 1) if is_prime(num)]

# Input from user - start and end
a = int(input("Enter the starting number (a): "))  
b = int(input("Enter the ending number (b): "))

# Output - getting the resul
result = primes_between(a, b)
print(f"Prime numbers between {a} and {b}: {result}")
       
