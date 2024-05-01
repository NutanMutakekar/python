''' vara Write a program to display all prime numbers within a range
Expected output:
Prime numbers between 25 and 50 are:
29
31
37
41
43
47'''

def is_prime(num):
    if num<= 1:
        return False
    for i in range(2,num//2):
        if num%i==0: 
            return False
    return True

def display_primes(start, end):
    print(f"Prime numbers between {start} and {end} are:")
    for num in range(start, end + 1):
        if is_prime(num):
            print(num)

start = 25
end = 50
display_primes(start, end)


#mine
import math

def prime(n):
    #! for single num
    # if n==1:
    #     return False
    if n==2 or n==3:
      return True
    elif n>3:
        for i in range(2,int(math.sqrt(n))+1):
           if n%i==0:
               return False
          
        return True
        
#! for range of nos
num = range(25,50)
prime_list = list(filter(prime, num))
print(prime_list)



#! for only one number
# num=2
# if prime(num):
#     print(num,"num is prime")
# else:
#      print(num,"num is not prime")
# prime_list=list(filter(prime,num))

