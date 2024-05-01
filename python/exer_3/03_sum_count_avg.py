#Write a program to count the total number of digits and sum of digits in a number and reverse the number

a=[6, 10, 30, 99, 45, 215, 69, 64, 175, 698, 399, 758, 892, 783, 72, 90]
print(a)
for i in a:
    if i%5==0:
        if i>500:
            break
        if i>150:
            continue
        elif i>500:
            break
        else:
            print("The number divisible by 5 is",i)
            

def count_digits(number):
    return len(str(number))

def sum_of_digits(number):
    total = 0
    for digit in str(number):
        total += int(digit)
    return total

def reverse_number(number):
    reversed_number = int(str(number)[::-1])
    return reversed_number

number = int(input("Enter a number: "))

digit_count = count_digits(number)
print("Total number of digits:", digit_count)

digit_sum = sum_of_digits(number)
print("Sum of digits:", digit_sum)

reversed_num = reverse_number(number)
print("Reversed number:", reversed_num)
