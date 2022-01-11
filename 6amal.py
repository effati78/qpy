import math

num1 = float(input("number 1: "))
num2 = float(input("number 2: "))

jam = num1 + num2
tafrigh = num1 - num2
zarb = num1 * num2
taghsim = num1 / num2
tavan = num1 ** num2
jazr1 = math.sqrt(num1)
jazr2 = math.sqrt(num2)

print('jam:', jam)
print('tafrigh:', tafrigh)
print('zarb:', zarb)
print('taghsim:', taghsim)
print('tavan:', tavan)
print('jazr ' + str(num1) + ' =', jazr1)
print('jazr ' + str(num2) + ' =', jazr2)
