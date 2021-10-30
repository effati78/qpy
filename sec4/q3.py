# سوال سه

number = input("Enter a number: ")

def change_number(n):
    if len(n) == 1:
        print("number is:", n)
        return 0

    n = n[-1:] + n[1:-1] + n[:1]
    print("number is:", n)

change_number(number)
