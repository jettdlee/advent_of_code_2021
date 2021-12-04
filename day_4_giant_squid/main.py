import pdb
import numpy as np
import re
from helpers.import_data import ImportData

class BingoParser:
    def __init__(self, dataset):
        self.dataset = dataset
        self.__setupNumberDraw()
        self.__setupBoards()

    def __setupNumberDraw(self):
        draw_row = self.dataset[0].split(",")
        self.draw = list(map(int, draw_row)) 

    def __setupBoards(self):
        self.boards = []
        board = []
        for row in self.dataset[2:]:
            if row == "":
                self.boards.append(board)
                board = []
            else:
                row = np.array(re.findall(r'\S+', row)).astype(int)
                board.append(row)
            
class BingoGame:
    def __init__(self, bingo_parser):
        self.number_draw = bingo_parser.draw
        self.game_boards = bingo_parser.boards
        self.board_states = {}

    def play(self):
        for drawn_number in self.number_draw:
            self.__checkBoards(drawn_number)
            # self.checkWinner()

    def __checkBoards(self, number):
        for board_index in range(len(self.game_boards)):
            board = self.game_boards[board_index]
            for row_index in range(len(board)):
                in_row_index = np.where(board[row_index] == number)
                if len(in_row_index) > 0:
                    self.board_states[board_index] = { row_index: 1 }


if __name__ == "__main__":
    data_file = ImportData('day_4.data', False)
    parser = BingoParser(data_file.dataset)
    game = BingoGame(parser)
    game.play()
