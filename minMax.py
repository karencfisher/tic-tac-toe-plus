import numpy as np


count = 0
max_depth = 3

def min_max(board, player, level, alpha = -1000, beta = 1000):
    global count
       
    #check board status
    winner = board.get_winner()
    if winner == 'X':
        return (-1, 100)
    if winner == 'O':
        return (-1, -100)
    if winner == 'T':
        return (-1, 0)

    availMoves = board.get_avail_moves()
    if len(availMoves) == 0:
        return (-1, 0)

    move_utils = board.get_utils(availMoves, player)
    best = np.argwhere(move_utils == np.amax(move_utils)).reshape(-1)
    availMoves = availMoves[best]

    if level > max_depth:
        availMoves = np.array([np.random.choice(availMoves)])
        
    if len(availMoves) == 1:
        if player == 'X':
            best = (availMoves[0], 100)
        else:
            best = (availMoves[0], -100)
    else:
        #list of moves evaluated
        moves = []
        #evaluate moves
        if player == "X":
            #maximizer 
            bestScore = -1000
            for m in availMoves:
                count += 1
                board.set_move(m, player) 
                score = min_max(board, "X", level+1, alpha, beta)
                moves.append((m, score[1]))
                board.clear_move(m)
                
                #do alpha beta pruning
                bestScore = max(bestScore, score[1])
                alpha = max(alpha, bestScore)
                if beta <= alpha:
                    break
            
        else:
            #minimizer
            bestScore = 1000
            for m in availMoves:
                count += 1
                board.set_move(m, player)
                score = min_max(board, "O", level+1, alpha, beta)
                moves.append((m, score[1]))
                board.clear_move(m)
                
                #do alpha beta pruning
                bestScore = min(bestScore, score[1])
                beta = min(beta, bestScore)
                if beta <= alpha:
                    break

        #pick best move
        if player == "X":
            best = max(moves, key=lambda v: v[1]) 
        else:
            best = min(moves, key=lambda v: v[1])  
              
    return best









    
    
