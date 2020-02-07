class ReversiBoard(object):

    BOARD_SIZE=8

    WHITE=1
    BLACK=2
    NONE=3

    def __init__(self):

        self.cells = []
        for i in range(self.BOARD_SIZE):
            self.cells.append([None for i in range(self.BOARD_SIZE)])

        self.cells[3][3] = self.WHITE
        self.cells[3][4] = self.BLACK
        self.cells[4][3] = self.BLACK
        self.cells[4][4] = self.WHITE

    def put_desc(self,x,y,color):
        if self.cells[x][y] is not None:
            return False


        flippable = self.flippable_list(x, y ,color)

        if flippable == []:
            return False
       
        self.cells[y][x] = color
        for x,y in flippable:
            self.cells[y][x] = color
        
        return True


    
    def flippable_list(self,x,y,color):

        PREV = -1
        NEXT = 1
        DERECTION = [PREV,0,NEXT]
        flippable =[]

        for dx in DERECTION:
            for dy in DERECTION:
                if dx == 0 and dy == 0:
                    continue

                inc = []
                depth = 0

                while(True):
                    depth +=1


                    rx = x + (dx * depth)
                    ry = y + (dy * depth)

                    if 0 <= rx < self.BOARD_SIZE and 0 <= ry < self.BOARD_SIZE:
                        request = self.cells[rx][ry]

                        if request is None:
                            break

                        if request == color:
                            if inc != []:
                                flippable.extend(inc)
                        
                        else:
                            inc.append((rx,ry))
        return flippable

    def show_board(self):
        print("--" * 20)
        for i in self.cells:
            for cell in i:
                if cell == self.WHITE:
                    print("W", end=" ")
                elif cell == self.BLACK:
                    print("B", end=" ")
                else:
                    print("*", end=" ")
            print("\n", end="")

                    



test = ReversiBoard()
test.show_board()
test.put_desc(3,5,1)
test.show_board()