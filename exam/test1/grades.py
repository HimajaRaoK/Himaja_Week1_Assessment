def get_input():
    name_student = input("Enter the student name: ")
    print("enter marks out of 100")
    s1 = input("Enter marks of subject 1: ")
    s2 = input("Enter marks of subject 2: ")
    s3 = input("Enter marks of subject 3: ")
    s4 = input("Enter marks of subject 4: ")
    s5 = input("Enter marks of subject 5: ")
    return name_student, s1, s2, s3, s4, s5

def compute_percentage(s1, s2, s3, s4, s5):
    sum_marks = int(s1) + int(s2) + int(s3) + int(s4) + int(s5)
    percentage = (sum_marks / 500) * 100
    print(f"The total marks are: {sum_marks}. The percentage is: {percentage}%")
    return percentage

def pass_fail(percentage):
    if percentage < 40:
        print("C - FAIL")
    elif percentage >= 40 and percentage < 70:
        print("B - PASS")
    else:
        print("A - OUTSTANDING")

def main():
    name_student, s1, s2, s3, s4, s5 = get_input()
    percentage = compute_percentage(s1, s2, s3, s4, s5)
    pass_fail(percentage)

main()
