def bill_splitter():
    total_amount=int(input("enter the total amount to be split: "))
    people=int(input("enter total amount of people: "))
    tip=int(input("enter tip percentage: "))

    if people<=0:
        print("number of people must be more than this")

    else:
        per_person = (total_amount + (total_amount * tip // 100)) // people
        print(f"\nEach person pays: {per_person} Rs")

bill_splitter()