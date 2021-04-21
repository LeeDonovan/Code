import random
import re
import time
import math
import itertools


class Mines:
    def __init__(self, gridsize, numberofmines):
        self.flags = []
        self.__currgrid = [[' ' for i in range(gridsize)] for i in range(gridsize)]
        self.__fail = False
        self.__currcell = (0, 0)
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
                self.__fail = True;

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
        if (x - 1) >= 0 and (x - 1) < gridsize:
            adjCells.append((x - 1, y))
        if (x + 1) >= 0 and (x + 1) < gridsize:
            adjCells.append((x + 1, y))
        if (y - 1) >= 0 and (y - 1) < gridsize:
            adjCells.append((x, y - 1))
        if (y + 1) >= 0 and (y + 1) < gridsize:
            adjCells.append((x, y + 1))
        if (x - 1) >= 0 and (x - 1) < gridsize:
            if (y - 1) >= 0 and (y - 1) < gridsize:
                adjCells.append((x - 1, y - 1))
        if (x - 1) >= 0 and (x - 1) < gridsize:
            if (y + 1) >= 0 and (y + 1) < gridsize:
                adjCells.append((x - 1, y + 1))
        if (x + 1) >= 0 and (x + 1) < gridsize:
            if (y - 1) >= 0 and (y - 1) < gridsize:
                adjCells.append((x + 1, y - 1))
        if (x + 1) >= 0 and (x + 1) < gridsize:
            if (y + 1) >= 0 and (y + 1) < gridsize:
                adjCells.append((x + 1, y + 1))


    def makeFrontier(sweeper):
        grid = sweeper
        gridBoard = grid.checkcell((0, 0))
        x = int(gridBoard[0][0])
        print(x)
        frontier = set()
        for r in range(gridsize):
            for c in range(gridsize):
                if gridBoard[r][c] != '0' and gridBoard[r][c] != ' ' and gridBoard[r][c] != 'F':
                    frontier.add((r, c))


    def getFlags(x, y, gridsize):  # returns flag count around a cell
        getAdjCells(x, y, gridsize)
        count = 0
        gridBoard = grid.checkcell((0, 0))
        # print("adjCells",adjCells)
        for i in adjCells:
            # print("i is = ",i," and >>>",gridBoard[adjCells[i][0]][adjCells[i][1]])

            if sweeper.flags.__contains__(i):
                count = count + 1
        return count




    gridsize = 24
    n_mines = 99
    sweeper = Mines(gridsize, n_mines)
    sweeper.showcurrent()

    stalemate = 0
    restarts = 0

    start_time = time.time()  # Time keeping variable.


    while not sweeper.checkmines():
        sweeper.flags.sort()
        #sweeper.mines.sort()

        if sweeper.checkmines():
            break

        adjCells = []
        adjClean = set()

        grid = sweeper
        gridBoard = grid.checkcell((0, 0))


        frontier = set()
        frontierList = []
        frontierDict = {}

        for r in range(gridsize):  # make frontier set()
            for c in range(gridsize):
                x = (r,c)
                if not sweeper.flags.__contains__(x):
                    if gridBoard[r][c] != '0' and gridBoard[r][c] != ' ':  # and gridBoard[r][c] != 'F':
                        frontier.add((r, c))

        print("frontier")
        print(frontier)

        for i in frontier:
            frontierList.append(i)

        print("frontierList", frontierList)

        for i in frontier:  # this will fill frontierDict with all {cell: [list of cells that are= ' ' and not flagged]}
            adjClean = set()
            adjCells = []
            x = i[0]
            y = i[1]
            getAdjCells(x, y, gridsize)
            adjClean = set()
            for j in adjCells:
                xx = (j[0],j[1])
                if not sweeper.flags.__contains__(xx):
                    if gridBoard[j[0]][j[1]] == ' ':
                        adjClean.add(j)
            if len(adjClean) == 0:
                frontierList.remove(i)
                continue
            adj = []
            for a in adjClean:
                adj.append(a)
            frontierDict.update({i: adj})

        # for i in frontier:
        #    getAdjCells(i[0], i[1], gridsize)
        print('frontierDict')
        print(frontierDict)

        frontDict = frontierDict

        fdict = len(frontierDict)
        print("fdict", fdict)
        list_f = []
        list_f = list(frontierDict.values())
        print("List\n", list_f)

        tfb = []
        tfb = set()  # set of the frontier blanks

        tempList1 = []
        removeThese = []
        for i in range(len(frontierList)):
            tempList1 = []
            tempList1 = frontierDict[ frontierList[i] ]
            if len(tempList1) == 0:
                removeThese.append(frontierList[i])
            else:
                for j in range(len(tempList1)):
                    if not sweeper.flags.__contains__(tempList1[j]):
                        tfb.add(tempList1[j])
        # print('tfb', tfb)
        for i in removeThese:
            for j in range(len(frontierList)):
                if frontierList[j] == i:
                    frontierList.remove(frontierList[j])
                    continue
        TFB = []  # list of the frontier blanks
        for i in tfb:
            TFB.append(i)
        TFB.sort()
        print("TFB", TFB)

        n = len(TFB)
        if n < 21:
            table = list(itertools.product([0, 1], repeat=n))
        elif n > 20:
            print("possible overflow avoided")
            table = list(itertools.product([0, 1], repeat=20))


        tempList2 = []
        tempList3 = []


        def getSum(l1, l2):  # l1 is list of index variables, l2 is table row
            c = 0
            for i in l1:
                c = c + l2[i]
            return c


        tableCheck = len(table)

        fdict = len(frontierDict)

        for i in range(len(frontierList)):  # where the sausage gets made. iterating through
            var = 0
            # print("list_f",list_f)
            # print("list_f[",i,"] ",list_f[i])
            # print("table size",len(table))

            tempList2 = []  # each cell and checking each blank
            tempList3 = []  # indexes of blank neighbors in TFB
            removeRows = []
            trueRows = []
            x = frontierList[i][0]
            y = frontierList[i][1]
            gridBoard = grid.checkcell((0, 0))
            cv = -1
            cv = int(gridBoard[x][y])
            flags = 0
            flags = getFlags(x, y, gridsize)
            #print(frontierList[i],"flags",flags)
            cv = cv - flags
            tempList2 = list_f[i]  # tempList2 is the blank neighbors of a cell
            # print(list_f[i])
            #print("Templist2 at", frontierList[i], tempList2)
            if (len(tempList2)) > 0:
                tempList3 = []
                for j in range(len(tempList2)):
                    var = -1
                    var = TFB.index(tempList2[j])
                    #print("var", var, "from cell", tempList2[j], "belonging to cell", frontierList[i])
                    if var < 20:
                        tempList3.append(var)
                    # print("xy =", x, y, "j=", j, "tempList2", tempList2)
                    # print("i =", i, "j=", j, "tempList3", tempList3)
                # tempList3.sort()
                if len(tempList3) > 0:
                    for row in table:
                        tempList4 = []
                        tempList4 = row
                        test = -1
                        test = getSum(tempList3, row)
                        if cv != test:
                            #print("frontierlist cell ", frontierList[i], " drops row ", row, " because ", cv, "!=", test,"targetcells", tempList3)
                            # removeRows.append(row)
                            continue
                        elif cv == test:
                            #print("frontierlist cell ", frontierList[i], "   keeps   ", row, " because ", cv, "=", test,"targetcells", tempList3)
                            trueRows.append(row)
                    #else:
                        #print("frontierlist cell ", frontierList[i], row, " cv ", cv, "test", test, "ELSE")
                table = trueRows
                # tempList3 = []
                # for i in range(len(removeRows)):
                #    table.remove(removeRows[i])

        print("table size", len(table))

        print("table", table)
        print("TFB", TFB)

        truthTableSums = []
        if (len(table) < tableCheck) and len(table) > 0:  # this will try to find consistency

            for i in range(len(table[0])):  # fills truthTableSums[] with 0s
                truthTableSums.append(0)

            for i in range(len(table[0])):
                for j in range(len(table)):
                    truthTableSums[i] = table[j][i] + truthTableSums[i]

        ttsPercent = []
        for i in range(len(truthTableSums)):
            x = truthTableSums[i] / int(len(table))
            ttsPercent.append(x)

        print("truthTableSums", truthTableSums)
        print("ttsPecent", ttsPercent)

        didAnythingChange = 0
        lowest = 1.0
        highest = 0.0
        for i in range(len(ttsPercent)):
            if i < 16:
                if ttsPercent[i] == 0.0:
                    sweeper.checkcell(TFB[i])
                    print("w/Certainty sweeper.checkcell", TFB[i])
                    sweeper.showcurrent()
                    didAnythingChange += 1
                    continue
                elif ttsPercent[i] == 1.0:
                    sweeper.flags.append(TFB[i])
                    print("w/Certainty flag ",TFB[i])
                    didAnythingChange += 1
                    continue
                if ttsPercent[i] < lowest:
                    lowest = ttsPercent[i]
                if ttsPercent[i] > highest:
                    highest = ttsPercent[i]

        if didAnythingChange == 0:
            if (1 - lowest) > highest:
                sweeper.checkcell(TFB[ttsPercent.index(lowest)])
                print("sweeper.checkcell", TFB[ttsPercent.index(lowest)])
                didAnythingChange = didAnythingChange + 1
            elif (1 - highest) < lowest:
                sweeper.flags.append(TFB[ttsPercent.index(highest)])
                print("new flag",TFB[ttsPercent.index(highest)], "and flags = ",flags)
                didAnythingChange = didAnythingChange + 1

            if (1-highest) == lowest and lowest < 0.5:
                sweeper.checkcell(TFB[ttsPercent.index(lowest)])
                print("sweeper.checkcell", TFB[ttsPercent.index(lowest)])
                didAnythingChange = didAnythingChange + 1

            elif (1-lowest) == highest and highest > 0.5:
                sweeper.flags.append(TFB[ttsPercent.index(highest)])
                print("new flag", TFB[ttsPercent.index(highest)], "and flags = ", sweeper.flags)
                didAnythingChange = didAnythingChange + 1

            if len(ttsPercent) == 0 and len(TFB) > 0:
                a = random.randint(0, len(TFB) - 1)
                sweeper.checkcell(TFB[a])
                print(" random sweeper.checkcell", TFB[a])
                didAnythingChange = didAnythingChange + 1

            else:
                if lowest == highest and lowest == 0.5 and highest == 0.5:
                    sweeper.checkcell(TFB[ttsPercent.index(lowest)])
                    print("50/50 sweeper.checkcell", TFB[ttsPercent.index(lowest)])
                    didAnythingChange = didAnythingChange + 1
        if didAnythingChange == 0:
            stalemate = stalemate + 1
            print("stalemate",stalemate)


        #stalemate path
        #nuclear fix
        if stalemate > 10:
            if sweeper.checkmines():
                break
            if len(set(sweeper.flags)) == n_mines:
                break
            grid = sweeper
            gridBoard = grid.checkcell((0, 0))
            for r in range(gridsize):  # make frontier set()
                for c in range(gridsize):
                    x = (r, c)
                    if gridBoard[r][c] == ' ':
                        if not sweeper.flags.__contains__(x):
                            print("stale mate, nuclear option check", x)
                            sweeper.checkcell(x)
                            break



        print("current")
        sweeper.showcurrent()
        print("flags at", sweeper.flags)
        print("flag count =",len(set(sweeper.flags)))
        print("restart count", restarts)


        if sweeper.isfail():
            sweeper = Mines(gridsize, n_mines)
            restarts = restarts + 1
            stalemate = 0
            print("RESTART #",restarts)#,"also current flags is",sweeper.flags)
            sweeper.showcurrent()

        sweeper.flags.sort()
        # sweeper.mines.sort()
        if sweeper.checkmines():
            break


        #this should be the right way to end it i think
        sweeper.flags.sort()

    print("END product")
    sweeper.showcurrent()
    print("flags at",sweeper.flags)
    print("restarts #",restarts)

    if sweeper.checkmines():
        print("TRUE end, restarts# =",restarts)
        grid = sweeper
        gridBoard = grid.checkcell((0, 0))
        for r in range(gridsize):  # make frontier set()
            for c in range(gridsize):
                if gridBoard[r][c] == ' ':
                    x = (r, c)
                    if not sweeper.flags.__contains__(x):
                        sweeper.checkcell(x)


    print("Gridsize",gridsize)
    print("n_mines",n_mines)
    print("Running time:", str(int((time.time() - start_time) * 1000)) + "ms")












    # list_f = list(frontierDict.values())
    # print("List\n", list_f)
    # print("list_f right before", list_f)
    # print(frontierList)
    # print("to start table size", len(table) )
    # xx=0
    # for row in table:
    #     print(row)
    #     xx = xx+ 1
    # print(xx)

    # print(len(list_f))
    # for g in range(fdict):
    #     p_list = list_f[g]
    #     print("plist: ", p_list)
    #     for h in range(1):
    #         x = 0
    #         x_list = []
    #         print("First part", list_f[g][0])
    #         x_p = list_f[g][h][0]
    #         y_p = list_f[g][h][1]
    #         x1 = gridBoard[x_p][y_p]
    #         if x == " ":
    #             print("It is a space")
    #             x = 0
    #             x_list.append(x)
    #         else:
    #             print("its something")
    #         print("Number x1 = ", x1)




    # while not sweeper.isfail():
    #     grid = sweeper
    #     gridBoard = grid.checkcell((0, 0))
    #
    #     for r in range(gridsize):
    #         for c in range(gridsize):
    #             if gridBoard[r][c] != '0' and gridBoard[r][c] != ' ' and gridBoard[r][c] != 'F':
    #                 frontier.add((r, c))
    #
    #     for i in frontier:  # this will fill frontierDict with all {cell: [list of cells that are= ' ']}
    #         adjClean.clear()
    #         adjCells.clear()
    #         x = i[0]
    #         y = i[1]
    #         getAdjCells(x, y, gridsize)
    #         adjClean.clear()
    #         for j in adjCells:
    #             if gridBoard[j[0]][j[1]] == ' ':
    #                 adjClean.add(j)
    #         adj = []
    #         for a in adjClean:
    #             adj.append(a)
    #         frontierDict.update({i: adj})



    # for row in table:
    #     print(row)

    # testD = {}
    # testL = [(0, 0), (0, 1), (1, 0), (1, 1)]
    # testD.update({(0, 0): []})
    # testD.update({(0, 1): []})
    # testD.update({(1, 0): [(0, 2), (1, 2)]})
    # testD.update({(1, 1): [(1, 2), (2, 1), (2, 0), (0, 2), (2, 2)]})

    #print("testD",testD)
    #tempList0 = testD[testL[2]]
    #print(tempList0)
