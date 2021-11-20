# سوال سه

import statistics

x = list()
n = int(input("N is: "))

for i in range(0, n):
    y = int(input())
    x.append(y)

k = int(input("K is: "))
z = x[:k]

average = statistics.mean(z)

print(x)
print(z)
print("average:", average)
