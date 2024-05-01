def count_case_letters(input_string):
    uppercase_count = 0
    lowercase_count = 0
    
    for char in input_string:
        if char.isupper():
            uppercase_count += 1
        elif char.islower():
            lowercase_count += 1
            
    return uppercase_count, lowercase_count


input_string = input("Enter a string: ")
uppercase_count, lowercase_count = count_case_letters(input_string)
print("Number of uppercase letters:", uppercase_count)
print("Number of lowercase letters:", lowercase_count)
