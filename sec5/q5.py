# سوال پنچ

x = list()
y = list()
n = float(input("Enter a number: "))

while n > 1:
    x.append(n)
    if n % 2:
        # odd
        y.append(int(3 * n))
    else:
        # even
        y.append(int(n / 2))

    n = float(input("Enter a number: "))

print(x)
print("final list: ", y)
