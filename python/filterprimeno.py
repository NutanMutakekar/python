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

