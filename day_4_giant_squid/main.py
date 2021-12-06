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
        self.winning_board = None
        self.check_winner = CheckWinner()

    def play(self):
        for drawn_number in self.number_draw:
            self.__markBoard(drawn_number)
            self.__checkWinner()
            if self.winning_board is not None:
                self.__calculateWinnings(drawn_number)
                break

    def __markBoard(self, number):
        for board_index in range(len(self.game_boards)):
            board = self.game_boards[board_index]
            for row_index in range(len(board)):
                in_row_index = np.where(board[row_index] == number)
                if len(in_row_index) > 0:
                    self.game_boards[board_index][row_index][in_row_index] = -1

    def __checkWinner(self):
        for board in self.game_boards:
            result = self.check_winner.check(board)
            if result == True:
                self.winning_board = board
    
    def __calculateWinnings(self, winning_number):
        sum_unmarked_numbers = 0
        for row in self.winning_board:
            unmarked_selections = np.delete(row, np.where(row == -1))
            sum_unmarked_numbers += np.sum(unmarked_selections)
        print('Sum of unmarked numbers: ', sum_unmarked_numbers)
        print('Winning numbers: ', winning_number)
        print('Final Score: ', sum_unmarked_numbers * winning_number)

        
class CheckWinner:
    def __init__(self):
        self.winning_condition = -5

    def check(self, board):
        if self.__checkHorizontal(board):
            return True 
        elif self.__checkVertical(board):
            return True 
        else:
            return False

    def __checkHorizontal(self, board):
        for row in board:
            if np.sum(row) == self.winning_condition:
                return True

    def __checkVertical(self, board):
        trans_board = np.transpose(board)
        for column in trans_board:
            if np.sum(column) == self.winning_condition:
                return True

if __name__ == "__main__":
    data_file = ImportData('day_4.data', False)
    parser = BingoParser(data_file.dataset)
    game = BingoGame(parser)
    game.play()
