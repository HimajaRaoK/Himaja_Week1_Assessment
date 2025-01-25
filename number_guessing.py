import random
def main():
    print("Welcome to number guessing game you have to guess a number between 1 and 100 \"only 3 tries are allowed\"")
    number=random.randint(1,100) 
    number_of_guesses=3
    while(number_of_guesses):
        guess=int(input("Enter your guess: "))
        if(guess==number):
            print("Congratulations! You guessed the number") 
            break
        elif(guess>number):
            print("Your guess is too high")
        else:
            print("Your guess is too low")
        number_of_guesses-=1
    if(number_of_guesses==0):   
        print(f"the number was {number}")
main() 