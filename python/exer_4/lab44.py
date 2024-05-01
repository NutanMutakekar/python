def is_palindrome(input_string):
    input_string = input_string.replace(" ", "").lower()
    return input_string == input_string[::-1]

input_string = input("Enter a string: ")
if is_palindrome(input_string):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
