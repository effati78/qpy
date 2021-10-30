# سوال شش

n = input("number: ")
x = int(input("which number? "))

def cut_number(n, x):
    if x == 0:
        x = 1

    xLength = len(n)
    print(n[xLength - x])

cut_number(n, x)
