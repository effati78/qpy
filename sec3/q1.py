# سوال یک

n = int(input("Enter a number: "))


def perfect_number(n):
    sum = 0
    for x in range(1, n):
        if n % x == 0:
            sum += x
    return sum == n


def perfect_number_0toN(n):
    for i in range(0, n):
        if perfect_number(i):
            print(i)


perfect_number_0toN(n)
