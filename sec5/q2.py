# سوال دو

x = list()
n = float(input("Enter a number (0 = end): "))

while n != 0:
    x.append(n)
    n = float(input())

z = list(dict.fromkeys(x))
half = len(x) / 2
for i in range(0, len(z)):
    temp = x.count(z[i])
    if temp > half:
        print("main element is: ", z[i])
