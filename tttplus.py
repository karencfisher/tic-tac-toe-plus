from board import Board
import minMax


class Game:
    def __init__(self, dims=3):
        self.wins = {'Computer':0, "Human":0, "Ties":0}
        self.board = Board(dims)

    def yesOrNo(self, prompt):
        while True:
            answer = input(prompt + ' ')                
            if not answer in ('yes', 'no'):
                print ("Please answer 'yes' or 'no'.")
            else:
                break
        return answer == 'yes'

    def __get_move(self, availMoves):
        while True:
            theirMove = int(input("Your move (O): "))
            if not theirMove in availMoves:
                print("Invalid move. Remaining moves are: ", availMoves)
            else:
                break
        return theirMove

    def play(self):
        self.board.clear_board()
        print(f'\n{self.board}')
        computerPlayFirst = self.yesOrNo("Do you want me to play first?")

        result = None
        firstMove = True
        while result is None:
            availMoves = self.board.get_avail_moves()
            if not computerPlayFirst or not firstMove:
                their_move = self.__get_move(availMoves)
                self.board.set_move(their_move, 'O')
                print(f'\n{self.board}')

                availMoves = self.board.get_avail_moves()
                result = self.board.get_winner()
                
            minMax.count = 0
            move = minMax.min_max(self.board, "X", 0)
            print("positions evaluated:", minMax.count)
            self.board.set_move(move[0], 'X')
            print(f'My move (X): {move[0]}\n')
            print(f'\n{self.board}')

            result = self.board.get_winner()
            firstMove = False
        
        if result == 'O':
            print('You won!')
            self.wins['Human'] += 1
        elif result == 'X':
            print('I won!')
            self.wins['Computer'] += 1
        else:
            print('No remaining winning moves, a tie.')
            self.wins['Ties'] += 1

                
def main():
    n_size = int(input('Dimension of board: '))
    game = Game(n_size)
    while True:
        game.play()         
        again = game.yesOrNo("Want to play again?")
        if not again:
            break

    for finalScore in game.wins:
        print(finalScore + ": " + str(game.wins[finalScore]))
    
if __name__ == '__main__':
    main()   
