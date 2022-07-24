## Tic Tac Toe Plus!

What makes Tic Tac Toe Plus is being able to play other than a 3x3 board. You can
play 4x4, 5x5, 6x6... (not tested beyond 6x6 yet though).

```
 O | X | X | O
---------------
 O | O | X | X
---------------
 X | O | O |
---------------
 O | O | X | X

No remaining winning moves, a tie.
Want to play again? no
Computer: 1
Human: 0
Ties: 1
```

Command line only at present. 

Play consists of a combination of heuristic -- calculation of the utility of available moves
based on how close the player is to completing a winning row, or is in danger of losing (blocking 
a threatening opponent) and min-max search with alpha-beta pruning. Still some bugs in the
heuristic calculations, so at present the "puny human" may on occassion win. (There is also 
at present a bug which may cause the computer to cheat at the last moment converting a human 
win to a tie.) But maybe friendly AI will let us win now and then, or cheat like a person may
if they think they can get away with it? ;)

To play, just clone repository and run on CLI:

```
python tttplus.py
```

And have fun!
