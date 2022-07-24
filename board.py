import numpy as np


class Board:
    def __init__(self, dimensions):
        self.__board = np.full((dimensions, dimensions), ' ')
        self.__dimensions = dimensions

    def __count_rows(self):
        filled_x = self.__board == 'X'
        filled_o = self.__board == 'O'
        
        rows_x = np.sum(filled_x, axis=1)
        rows_o = np.sum(filled_o, axis=1)
        rows = np.vstack((rows_x, rows_o))

        cols_x = np.sum(filled_x, axis=0)
        cols_o = np.sum(filled_o, axis=0)
        cols = np.vstack((cols_x, cols_o))

        d1 = (np.sum(np.diagonal(filled_x)), 
                     np.sum(np.diagonal(filled_o)))

        d2 = (np.sum(np.diagonal(np.fliplr(filled_x))), 
              np.sum(np.diagonal(np.fliplr(filled_o))))

        return rows, cols, d1, d2

    def __map_move_to_xy(self, move):
        x = move % self.__dimensions
        y = move // self.__dimensions
        return x, y

    def __str__(self):
        output = []
        for row in range(self.__dimensions):
            pieces = [self.__board[row][i] for i in range(self.__dimensions)]
            row_str = ' ' + ' | '.join(pieces) + '\n'
            output.append(row_str)
            if row < self.__dimensions - 1:
                length = 4 * self.__dimensions - 1
                line = '-' * length + '\n'
                output.append(line)
        return ''.join(output)
        
    def get_avail_moves(self):
        squares = self.__board.reshape(-1)
        avail = np.argwhere(squares == ' ')
        return avail.reshape(-1)

    def set_move(self, move, player):
        x, y = self.__map_move_to_xy(move)
        self.__board[y, x] = player

    def clear_move(self, move):
        x, y = self.__map_move_to_xy(move)
        self.__board[y, x] = ' '

    def clear_board(self):
        self.__board.fill(' ')

    def get_winner(self):
        rows, cols, d1, d2 = self.__count_rows()
        rows_x = np.concatenate((rows[0], cols[0], [d1[0]], [d2[0]]))
        rows_o = np.concatenate((rows[1], cols[1], [d1[1]], [d2[1]]))
        if any(rows_x == self.__dimensions):
            winner = 'X'
        elif any(rows_o == self.__dimensions):
            winner = 'O'
        elif all(rows_x > 0) and all(rows_o > 0):
            winner = 'T'
        else:
            winner = None
        return winner

    def get_utils(self, moves, player):
        if player == 'X':
            me = 0
            they = 1
        else:
            me = 1
            they = 0

        utils = np.zeros(len(moves), dtype=int)
        rows, cols, d1, d2 = self.__count_rows()
        for index in range(len(moves)):
            x, y = self.__map_move_to_xy(moves[index])
            if rows[they, y] == self.__dimensions - 1:
                util = 100
            else:
                util = 0 if rows[they, y] > 0 else rows[me, y] + 1

            if cols[they, x] == self.__dimensions - 1:
                util = 100
            else:
                util += 0 if cols[they, x] > 0 else cols[me, x] + 1

            d_l = [i for i in range(self.__dimensions)]
            d1_l = [(i, i) for i in d_l]
            if (y, x) in d1_l:
                if d1[1] == self.__dimensions - 1:
                    util = 100
                else:
                    util += 0 if d1[they] > 0 else d1[me] + 1

            d2_l = [(i, j) for i, j in zip(d_l, d_l[::-1])]
            if (y, x) in d2_l:
                if d2[1] == self.__dimensions - 1:
                    util = 100
                else:
                    util += 0 if d2[they] > 0 else d2[me] + 1

            utils[index] = util
        return utils



def tests():
    board = Board(4)
    print(board)

    board.set_move(3, 'X')
    board.set_move(2, 'X')
    board.set_move(10, 'O')
    print(f'\n{board}')

    board.clear_move(2)
    print(f'\n{board}')

    board.clear_board()
    print(f'\n{board}')

    for i in range(4):
        board.set_move(i, 'X')
    print(f'\n{board}')
    print(f'winner is {board.get_winner()}')

    board.clear_board()
    board.set_move(0, 'X')
    board.set_move(3, 'X')
    board.set_move(4, 'O')
    board.set_move(5, 'X')
    board.set_move(12, 'X')
    print(f'\n{board}')

    m = board.get_avail_moves()
    print(m)
    print(board.get_utils(m))

    board.clear_board()
    board.set_move(0, 'O')
    board.set_move(2, 'X')
    board.set_move(5, 'O')
    board.set_move(8, 'X')
    board.set_move(15, 'O')
    print(f'\n{board}')

    m = board.get_avail_moves()
    print(m)
    print(board.get_utils(m))




if __name__ == '__main__':
    tests()



    