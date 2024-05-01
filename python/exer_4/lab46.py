def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def separate_prime_nonprime(input_list):
    prime_numbers = []
    non_prime_numbers = []
    for num in input_list:
        if is_prime(num):
            prime_numbers.append(num)
        else:
            non_prime_numbers.append(num)
    return prime_numbers, non_prime_numbers

n = int(input("Enter the number of values: "))
values = []
for i in range(n):
    value = int(input("Enter value {}: ".format(i + 1)))
    values.append(value)

prime_numbers, non_prime_numbers = separate_prime_nonprime(values)
print("Prime numbers:", prime_numbers)
print("Non-prime numbers:", non_prime_numbers)
print(type(value))
print(type(values))


