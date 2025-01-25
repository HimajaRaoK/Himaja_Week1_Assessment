def leap_year(year):
    return (year % 4 == 0 )   #to check if its a leap year or not - 4 because leap year occurs for every 4 years

for _ in range(1):  # we can change this range if we want - it determines the number of inputs it takes from users
    year = int(input("Enter a year: "))
    print(f"{year} is a leap year." if leap_year(year) else f"{year} is not a leap year.")
