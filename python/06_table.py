'''Write a program to print multiplication table of a given number
For example, num = 2 so the output should be
1x2=2
2x2=4
3x2=6
4x2=8
5x2=10
6x2=12
7x2=14
8x2=16
9x2=18
10x2=20'''

def multiplication_table(num):
    for i in range(1, 11):
        result = i * num
        print(f"{i} x {num} = {result}")

num = 2
multiplication_table(num)
