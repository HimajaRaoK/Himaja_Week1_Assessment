def check_balance(balance):
    print(f"current balance is: {balance}rs")

def deposit_money(balance):
    amount=int(input("enter money to be deposited: "))
    balance=balance+amount
    print(f"deposited money is {amount} and the updated balance is {balance}")
    return balance

def withdraw_money(balance):
    amount=int(input("enter money to be withdran: "))
    if (amount>balance):
        print("please enter right amount")
    else:
        balance=balance-amount
        print(f"withdrawn money is {amount} and updated balance is {balance}")
    return balance

def atm():
    balance=0
    while True:
        print("choose the options")
        print("1.check balance")
        print("2.Deposit")
        print("3.Withdraw")
        print("4. Exit")
        choice=input("enter choice: ")

        if choice=='1':
            check_balance(balance)

        elif choice=='2':
            balance=deposit_money(balance)
        
        elif choice=='3':
            balance=withdraw_money(balance)

        elif choice=='4':
            print("exiting....")
            break

        else:
            print("wrong choice")

atm()


