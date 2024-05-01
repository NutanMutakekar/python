# def checkCap(n):
#     for i in n:
#         if n[i].isupper():
#             cc+=int(i)
#             return cc
#         elif n[i].islower():
#              cl+=int(i)
#              return cl
# cc=0
# cl=0
# name="NUtan"
# checkCap(name)
# print("capital letter is:",cc)
# print("small letter is:",cl)

def checkCap(n):
    cc = 0
    cl = 0
    for i in n:
        if i.isupper():
            cc += 1
        elif i.islower():
            cl += 1
    return cc, cl

name = "NUtan"
a,b = checkCap(name)
print("capital letter is:", a)
print("small letter is:", b)
