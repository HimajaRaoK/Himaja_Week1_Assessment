def fizz_buzz(n):
    if n%3==0 and n%5==0:
        print("FIZZBUZZ")
    if n%3==0:
        print("FIZZ")
    if n%5==0:
        print("BUZZ")
    else:
        return n
    
def fizzorbuzz():
    for i in range(1,101):
        print(fizz_buzz(i))

fizzorbuzz()