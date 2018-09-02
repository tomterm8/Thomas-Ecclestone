# a project to create a simple minesweeper simulation game

import random

maxX = 6 # this is the size of the grid
maxY = 6

a = 0


# mineCell is a basic class that we use to contain
# all basic information about a specific cell

class mineCell:

    x=0
    y=0
    mine = 0
    neighbours = 0
    revealed = False

    def __init__(self,x,y,isMine):
        self.x = x
        self.y = y
        self.mine = isMine

# myBoard is an aggregate class containing lists that function
# as a board of mineCells

class myBoard:

    # we are using a list to define
    board = list()
    line = list()


    # an constructor that creates a board full of mineCells
    def __init__(self):

        for Y in range(0,maxX):

            for X in range(0,maxY):
                # just a random number generator that will make every
                # 4th cell a mine.
                if random.randint(0,3) == 2:
                    n = 1
                else:
                    n = 0


                #create a new mineCell
                a = mineCell(X,Y,n)
                # add it to the line ()
                self.line.append(a)
            #add each line to the board
            self.board.append(self.line)
            self.line = list()

    # this function prints the location of mines
    def printBoardMines(self):
        print("Here")

        res = list()

        for line in self.board:

            for eachCell in line:

                if eachCell.revealed == False:
                    res.append('--[' + str(eachCell.mine) + ']~+' + str(eachCell.neighbours))
                else:
                    res.append('00[' + str(eachCell.mine) + ']~+' + str(eachCell.neighbours))
            print(res)
            res = list()

    # a function that creates a minimum range value
    def minRange(self,min, val):
        if val < min:
            return(min)
        else:
            return(val)
    # a function that creates a maximum range value
    def maxRange(self,max, val):
        if val > max:
            return(max)
        else:
            return(val)

    # a function that calculates if a cell has neighbours that have mines
    def CalculateCellNeighbours(self,X,Y):
        tot = 0

        #calculate ranges of the map
        minRangeX = self.minRange(X-1,0)
        maxRangeX = self.maxRange(X+1,maxX+1)
        minRangeY =  self.minRange(Y-1,0)
        maxRangeY = self.maxRange(Y+1,maxY+1)

        for line in self.board:

            for eachCell in line:
                if eachCell.x in range(minRangeX, maxRangeX + 1) and eachCell.y in range(minRangeY, maxRangeY + 1):
                     print('debug y', eachCell.y, 'x',eachCell.x,'has', eachCell.mine )
                     tot += eachCell.mine

        self.board[Y][X].neighbours= tot - self.board[Y][X].mine

        #print('square X',X,'Y',Y, 'has ', tot, 'neighbouring mines')
        #print('min Y',minRangeY ,'max Y',maxRangeY, 'min X',minRangeX, 'max X',maxRangeX)

    # a function to calculate all neighbour values of mines
    def CalculateAllNeighbours(self):
        for x in range(0, maxX):
            for y in range(0, maxY):
                self.CalculateCellNeighbours(x,y)

    #actually checks if cell has a mine in it
    def tryReveal(self,x,y):

        if self.board[y][x].mine == 1:
            print('Lost it, douchebag')
            sys.exit()
        else:
            print('DEBUG',y,x,self.board[y][x].revealed)
            self.board[y][x].revealed == True

a = myBoard()
a.printBoardMines()

#a.CalculateCellNeighbours(2,2)
a.CalculateAllNeighbours()
#a.tryReveal(2,2)
a.printBoardMines()
