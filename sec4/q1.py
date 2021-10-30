# سوال یک

def perfect_number(n):
    sum = 0
    for x in range(1, n):
        if n % x == 0:
            sum += x
    return sum == n

def perfect_number_4digit():
    total = 0

    for i in range(999, 10000):
        if perfect_number(i):
            print('perfect number is:', i)

            for j in range(0, 4):
                i = str(i)
                total += int(i[j])

    print('total is:', total)

perfect_number_4digit()
