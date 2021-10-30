# سوال یک

number = []
score = []
n = int(input("How many students do you want to enroll? "))

for i in range(0, n):
    numberInput = int(input("student number: "))
    scoreInput = float(input("average: "))

    number.append(numberInput)
    score.append(scoreInput)

maxScore = max(score)
indexScore = score.index(maxScore)
bestnumber = number[indexScore]

print("the best student:", bestnumber)
print("average:", maxScore)
