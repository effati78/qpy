# سوال دو

n = int(input("enter a n value: "))
d = {}

for i in range(n):
    keys = input()
    values = int(input())
    d[keys] = values

print(d)

new_list = list(d.items())
print(new_list)
