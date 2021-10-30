# سوال دو

n = int(input("How many numbers do you want to enter? "))


def perfect_number(n):
    sum = 0
    for x in range(1, n):
        if n % x == 0:
            sum += x
    return sum == n


for i in range(0, n):
    number = int(input("number: "))
    print(perfect_number(number))
