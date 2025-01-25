def loan_eligibility():
    salary=int(input("Enter your salary: "))
    age=int(input("enter your age"))
    credit_score=int(input("enter your credit score"))

    if age<21:
        print("rejected - age must be above 21")

    elif salary<100000:
        print("rejected - salary must be above 1 lakh")

    elif credit_score<1000:
        print("rejected - credit must be higher than 1000")

    else:
        print("Loan approved successfully- all conditions are satisfied")

loan_eligibility()
