# سوال چهار

a = int(input('Enter A: '))
b = int(input('Enter B: '))

def swapـnumbers(a, b):
    [a, b] = [b, a]
    print("number A is:", a)
    print("number B is:", b)

swapـnumbers(a, b)