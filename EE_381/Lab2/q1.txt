import random

people = []
trials = 10000000
numOfA = 0
numOfB = 0
numOfC = 0
A = 500
B = 300
C = 200
for i in range(A):
    people.append('A')
for i in range(B):
    people.append('B')
for i in range(C):
    people.append('C')
random.shuffle(people)
for i in range(trials):
    group = random.sample(people, 4)
    if all(person == 'A' for person in group):
        numOfA += 1
    elif all(person == 'B' for person in group):
        numOfB += 1
    elif all(person == 'C' for person in group):
        numOfC += 1
print("Number of groups that are all A: ", numOfA)
print("Number of groups that are all B: ", numOfB)
print("Number of groups that are all C: ", numOfC)
print("Probability of A is", numOfA/trials)
print("Probability of B is", numOfB/trials)
print("Probability of C is", numOfC/trials)
