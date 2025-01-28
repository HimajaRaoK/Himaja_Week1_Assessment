while True:
    user_input = input("Enter a string or number (or type 'exit' to quit): ")

    if user_input.lower() == 'exit':
        break
    if user_input == user_input[::-1]:
        print(f"'{user_input}' is a palindrome!")
    else:
        print(f"'{user_input}' is not a palindrome.")

