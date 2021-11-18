# سوال یک

x = list()
n = float(input("Enter a number (0 = end): "))

while n != 0:
    x.append(n)
    n = float(input())

print(x)
temp = x[0]
del x[0]
x.append(temp)
print(x)
