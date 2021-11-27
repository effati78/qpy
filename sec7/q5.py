# سوال پنج

import statistics
student = [{"name": "ali", "moadel": 20}, {"name": "hasan", "moadel": 15}]

print(student)
n = int(input("1: Student information \n2: Delete student \n3: Average of all students \nChoose an option: "))
a = []

for x in range(len(student)):
    a.append(student[x]["moadel"])

if(n == 1):
    print(student)
elif(n == 2):
    x = int(input("x: "))
    del student[x]
    print(student)
elif(n == 3):
    print(statistics.mean(a))
