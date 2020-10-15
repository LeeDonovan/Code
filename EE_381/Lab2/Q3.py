import random

trials = 1000000
wins = 0;
print("Pick 4 different numbers, 1 through 20")
picks = []
numbers = []

for i in range(20):
    numbers.append(i+1)
print(numbers)

for i in range(4):
    num = int(input())
    picks.append(num)

for i in range(trials):
    lottery = random.sample(numbers,4)
    if (set(lottery) == set(picks)):
        wins += 1

print(wins)
print("Out of",trials,"trials, there were",wins,"wins")
print("Probability:", wins/trials)
