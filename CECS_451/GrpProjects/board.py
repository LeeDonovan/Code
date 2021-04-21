import random
import numpy as np
import time

class Board:
    def __init__(self, n):
        self.n_queen = n
        self.map = [[0 for j in range(n)] for i in range(n)]
        self.fit = 0
    
        for i in range(self.n_queen):
            j = random.randint(0, self.n_queen - 1)
            self.map[i][j] = 1

    def fitness(self):    
        self.fit=0    
        for i in range(self.n_queen):
            for j in range(self.n_queen):
                if self.map[i][j] == 1:
                    for k in range(1, self.n_queen - i):
                        if self.map[i + k][j] == 1:
                            self.fit += 1
                        if j - k >= 0 and self.map[i + k][j - k] == 1:
                            self.fit += 1
                        if j + k < self.n_queen and self.map[i + k][j + k] == 1:
                            self.fit += 1

    def show(self):
        print(np.matrix(self.map))
        print("Fitness: ",  self.fit)

    def flip(self, i, j):
        if self.map[i][j] == 0:
            self.map[i][j] = 1
        else:
            self.map[i][j] = 0

    def get_map(self):
        return self.map
    
    def get_fit(self):
        return self.fit


class hill:

    def __init__(self):
        self

    def hillClimb():
        t0 = time.clock()
        current = Board(5)
        current.fitness()
        fit = current.fit
        current.show()
        restart = 0
        while current.fit != 0:
            current.fitness()
            fit = current.fit
           # print("restarts are at #:",restart)
            #current.show()

            for i in range(current.n_queen):
                for j in range(current.n_queen):
                    if current.map[i][j] == 1:
                        current.map[i][j] = 0
                        jj = (j+1) % 5
                        current.map[i][jj] = 1
                        current.fitness()
                        tempfit = current.fit
                        if tempfit < fit:
                            neighbor = current
                            current = neighbor
                            current.fitness()
                            fit = current.fit
                            continue
                        if current.fit == 0:
                            break
            if fit != 0:
                restart = restart + 1
                current = Board(5)
                current.fitness()
        current.fitness()
        if current.fit == 0:
          print("final product")
          print("restarts are at #:",restart)
          print("Time: " + time.clock() - t0)
          current.fitness()
          current.show()
            
if __name__ == '__main__':
    test = Board(5)
    test.fitness()
    test.show() 
    test1 = hill
    test1.hillClimb()