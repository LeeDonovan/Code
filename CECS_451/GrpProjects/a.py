import random
import numpy as np


def genetic(self):
  encode = []
  boards = []
  selection = 0
  for i in range(8):
    num = ""
    for i in self.get_map():
      rInt = str(random.randint(1,5))
      num+= rInt
    encode.append(num)
  for i in encode:
    temp = Board(5)
    temp.blank()
    temp.fitness()
    print(i)
    temp.fill(i)
    boards.append(temp)
  for i in boards:
    i.fitness()
    selection+=i.select
    i.show()