import random
kids = []
trials = 100000
same = 0
n = int(input("Choose an n: (10 or 50)"))
boys = 2*n
girls = 2*n
for i in range(boys):
    kids.append('B')
for i in range(girls):
    kids.append('G')
random.shuffle(kids)
for i in range(trials):
    group = random.sample(kids,2*n)
    if  group.count('B') == group.count('G'):
        same += 1
print("In",trials,"trials, the number of groups that contain an equal number of boys and girls:", same)
print("Probability:", same/trials)

