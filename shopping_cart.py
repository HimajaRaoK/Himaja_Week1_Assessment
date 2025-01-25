def add_item():
    name=input("enter name of the item: ")
    price=int(input("enter its price: "))
    return name,price

def view_cart(cart):
    if len(cart)==0:
        print("no items present in cart")
    else:
        for item in cart:
            print(f"item: {item[0]}-{item[1]}rs")

def compute_total(cart):
    total=0
    for item in cart:
        total=total+item[1]
    print(f"the total price is {total}rs")

def shopping_cart():
    cart=[]
    while True:
        print("select the options: ")
        print("1.Add item")
        print("2.View Cart")
        print("3.Total amount")
        print("4.Exit")
        choice=input("enter ur choice:")

        if choice=='1':
            name,price=add_item()
            cart.append((name,price))
        
        elif choice=='2':
            view_cart(cart)

        elif choice=='3':
            compute_total(cart)

        elif choice=='4':
            print("exit....")
            break

        else:
            print("enter right choice")

shopping_cart()
