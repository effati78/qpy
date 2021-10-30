# سوال سه

import math

n = int(input("Enter a number: "))

def square_number(number):
    root = math.sqrt(number)
    return int(root + 0.5) ** 2 == number

def square_number_0toN(n):
     for i in range(0, n):
        if square_number(i):
            print(i)

square_number_0toN(n)
