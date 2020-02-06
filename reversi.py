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

    def start(self):
        print(12345)
        pass

print(7777)


test=ReversiBoard()
test.start()
