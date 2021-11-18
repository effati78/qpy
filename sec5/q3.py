# سوال سه


def is_arithmetic(l):
    delta = l[1] - l[0]
    for index in range(len(l) - 1):
        if not (l[index + 1] - l[index] == delta):
            return False
    return True


x = list()
n = float(input("Enter a number (0 = end): "))

while n != 0:
    x.append(n)
    n = float(input())

print(is_arithmetic(x))
