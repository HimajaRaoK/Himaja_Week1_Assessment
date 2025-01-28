n=int(input("enter the number for getting multiplication tables: "))

def multiply(n):
    for i in range(1,11):
        print(f"{n}x{i}={n*i}")

multiply(n)