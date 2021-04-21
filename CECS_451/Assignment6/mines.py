import random
import re
import time
 
 
class Mines:
    def __init__(self, gridsize, numberofmines):
        self.flags = []
        self.__currgrid = [[' ' for i in range(gridsize)] for i in range(gridsize)]
        self.__fail = False;
        self.__currcell = (0,0)
        emptygrid = [['0' for i in range(gridsize)] for i in range(gridsize)]
        self.__mines = self.__getmines(emptygrid, self.__currcell, numberofmines)        
        for i, j in self.__mines:
            emptygrid[i][j] = 'X'
        self.__grid = self.__getnumbers(emptygrid)                
 
        
    def __getrandomcell(self, grid):
        gridsize = len(grid)
 
        a = random.randint(0, gridsize - 1)
        b = random.randint(0, gridsize - 1)
 
        return (a, b)
 
    def __getneighbors(self, grid, rowno, colno):
        gridsize = len(grid)
        neighbors = []
 
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i == 0 and j == 0:
                    continue
                elif -1 < (rowno + i) < gridsize and -1 < (colno + j) < gridsize:
                    neighbors.append((rowno + i, colno + j))
                    
        return neighbors
    
 
    def __getmines(self, grid, start, numberofmines):
        mines = []
        neighbors = self.__getneighbors(grid, *start)
 
        for i in range(numberofmines):
            cell = self.__getrandomcell(grid)
            while cell == start or cell in mines or cell in neighbors:
                cell = self.__getrandomcell(grid)
            mines.append(cell)
            
        return mines
    
 
    def __getnumbers(self, grid):
        for rowno, row in enumerate(grid):
            for colno, cell in enumerate(row):
                if cell != 'X':
                    values = [grid[r][c] for r, c in self.__getneighbors(grid, rowno, colno)]
                    grid[rowno][colno] = str(values.count('X'))
                    
        return grid
    
    
    def __showcells(self, rowno, colno):        
        if self.__currgrid[rowno][colno] != ' ':
            return
 
        self.__currgrid[rowno][colno] = self.__grid[rowno][colno]
 
        if self.__grid[rowno][colno] == '0':
            for r, c in self.__getneighbors(self.__grid, rowno, colno):
                if self.__currgrid[r][c] != 'F':
                    self.__showcells(r, c)
                    
 
    def __showgrid(self, grid):
        gridsize = len(grid)
        horizontal = '   ' + (4 * gridsize * '-') + '-'
        toplabel = '     '
 
        for i in range(gridsize):
            if i < 10:
                toplabel = toplabel + str(i) + '   '
            else:
                toplabel = toplabel + str(i) + '  '
 
        print(toplabel + '\n' + horizontal)
 
        for idx, i in enumerate(grid):
            row = '{0:2} |'.format(idx)
            for j in i:
                row = row + ' ' + j + ' |'
 
            print(row + '\n' + horizontal)
 
        print('')
    
 
    def checkcell(self, cell):
        if not self.__fail:            
            self.__currcell = cell
            if self.__grid[cell[0]][cell[1]] == 'X':
                self.__fail = True
                
        return self.__currgrid
 
 
    def showcurrent(self):        
        self.__showcells(*self.__currcell)
        self.__showgrid(self.__currgrid)
 
    
    def isfail(self):
        return self.__fail
 
 
    def checkmines(self):
        if set(self.__mines) == set(self.flags):
            return True
        else:
            return False

    
 
        
if __name__ == '__main__':

  def getAdjCells(x, y, gridsize):

    adjCells.clear()
    if (x - 1) >=0 and (x - 1) < gridsize:
      adjCells.add((x-1,y))
    if (x + 1) >=0 and (x + 1) < gridsize:
      adjCells.add((x+1,y))
    if (y - 1) >=0 and (y - 1) < gridsize:
      adjCells.add((x,y-1))
    if (y + 1) >=0 and (y + 1) < gridsize:
        adjCells.add((x,y+1))
    if (x - 1) >= 0 and (x - 1) < gridsize:
      if (y - 1) >= 0 and (y - 1) < gridsize:
        adjCells.add((x - 1, y - 1))
    if (x - 1) >= 0 and (x - 1) < gridsize:
      if (y + 1) >= 0 and (y + 1) < gridsize:
        adjCells.add((x - 1, y + 1))
    if (x + 1) >= 0 and (x + 1) < gridsize:
      if (y - 1) >= 0 and (y - 1) < gridsize:
        adjCells.add((x + 1, y - 1))
    if (x + 1) >= 0 and (x + 1) < gridsize:
      if (y + 1) >= 0 and (y + 1) < gridsize:
        adjCells.add((x + 1, y + 1))


  def makeFrontier(sweeper):
      grid = sweeper
      gridBoard = grid.checkcell((0, 0))
      x = int(gridBoard[0][0])
      print( x)
      frontier = set()
      for r in range(gridsize):
          for c in range(gridsize):
              if gridBoard[r][c] != '0' and gridBoard[r][c] != ' ' and gridBoard[r][c] != 'F':
                  frontier.add((r, c))

  gridsize = 8
  n_mines = 40
  sweeper = Mines(gridsize, n_mines)
  sweeper.showcurrent()

  adjCells = set()
  adjClean = set()

  grid = sweeper
  gridBoard = grid.checkcell((0, 0))
  x = int(gridBoard[0][0])
  print("gridboard = ", x)

  frontier = set()
  frontierDict = {}

  for r in range(gridsize):
      for c in range(gridsize):
          if gridBoard[r][c] != '0' and gridBoard[r][c] != ' ' and gridBoard[r][c] != 'F':
              frontier.add((r,c))
  #print(frontier)



  count = 0
  for i in frontier: #this will fill frontierDict with all {cell: [list of cells that are= ' ']}
    adjClean.clear()
    x = i[0]
    y = i[1]
    getAdjCells(x,y,16)
    #print(adjCells)

    for j in adjCells:
      if gridBoard[j[0]][ j[1]] == ' ':
        adjClean.add(j)
    print(count)
    print(adjClean)
    adj =[]
    for a in adjClean:
      adj.append(a)
    x = {i:adj}
    frontierDict.update(x)
    count+=1

  print('frontierDict')
  print(frontierDict)

  fdict = len(frontierDict)
  list_f = list( frontierDict.values())
  print("List\n",list_f)
  print(len(list_f))
  for g in range(fdict):
      p_list = list_f[g]
      print("plist: ", p_list)
      for h in range(1):
        x = 0
        x_list = []
        print("First part" ,list_f[g][0])
        x_p = list_f[g][h][0]
        y_p = list_f[g][h][1]
        x1 = gridBoard[x_p][y_p]
        if x == " ":
            print("It is a space")
            x = 0
            x_list.append(x)
        else:
            print("its something")
        print("Number x1 = ", x1)