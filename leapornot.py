def leap_year_or_not(year):
    return (year%4==0)

for i in range(2):
    year=int(input("enter the year: "))
    print(f"{year} is a leap year"if leap_year_or_not(year) else f"{year} is not a leap year")