# Exam
# سوال چهار

A = {'a', 'd', 'c'}
B = {'a', 'b', 'h'}

q = A & B #q = (A ∩ B)
z = A | B #z = (A ∪ B)
w = A - B #w = (A - B)

# (A ∩ B) ∪ (A - B) => q ∪ w
o = q | w # q ∪ w

print(o)