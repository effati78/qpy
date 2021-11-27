# Exam
# سوال سه

str = input()
n = int(input("n: "))
isupper_count = 0
islower_count = 0

for x in range(n):
    if(str[x].isupper()):
        isupper_count += 1        

    if(str[x].islower()):
        islower_count += 1  

print('isupper:', isupper_count)
print('islower:', islower_count)
        