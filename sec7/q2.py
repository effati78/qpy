# سوال دو

from random import randrange
def perfect_number(n):
    sum = 0
    for x in range(1, n):
        if n % x == 0:
            sum += x
    return sum == n

n = int(input("n: "))
rand_list = []
perfect_list = []

for x in range(n):
    rand_list.append(randrange(100))

print(rand_list)
for y in range(len(rand_list)):
    if(perfect_number(rand_list[y])):
        perfect_list.append(rand_list[y])

if(len(perfect_list) > 0):
    print(perfect_list)
else:
    print('empty')
