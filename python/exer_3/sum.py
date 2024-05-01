# n = int(input("Enter a positive integer n: "))
# sum_n = 0
# for i in range(1, n+1):
#     sum_n += i
# average_n = sum_n / n
# cube_n = sum_n ** 3

# print(f"Sum of the first {n} natural numbers is: {sum_n}")
# print(f"Average of the first {n} natural numbers is: {average_n}")
# print(f"Cube of the sum of the first {n} natural numbers is: {cube_n}")



numbers=[24,56,152,215,54,35,25,555,655]

# for i in range (0,len(list1)) :
#     # print(list1[i])
#     if list1[i]%5==0:
#         print(list1[i])
#         if list1[i]>150:
#             list1[i]
#             continue     
#         if list1[i]>500:
#             list1[i]
#             exit

# numbers = [10, 25, 30, 60, 80, 200, 300, 550, 600]

# for num in numbers:
#     if num % 5 == 0:
#         if num > 500:
#             break
#         if num > 150:
#             continue
#         print(num)


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
# print("Sum of digits:", digit_sum)
print("Sum of digits:", sum_of_digits(number))

reversed_num = reverse_number(number)
# print("Reversed number:", reversed_num)
print("Reversed number:", reverse_number(number))

       

 