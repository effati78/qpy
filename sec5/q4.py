# سوال چهار


def is_geometric(li):
    if len(li) <= 1:
        return True

    ratio = li[1] / float(li[0])
    for i in range(1, len(li)):
        if li[i] / float(li[i - 1]) != ratio:
            return False
    return True


x = list()
n = float(input("Enter a number (0 = end): "))

while n != 0:
    x.append(n)
    n = float(input())

print(is_geometric(x))
