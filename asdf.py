p, board, pe = 0, ["-" for i in range(9)], "XO"
def printb(b):
    for i in range(9):
        print(b[i], end='')
        if (i+1)%3==0:
            print()
while True:
    inp = int(input("Player " + pe[p] + " play: "))
    win = False
    valid = False
    if(board[inp-1] == "-"):
        board[inp-1] = pe[p]
        valid = True
    printb(board)
    for i in range(3):
        if board[i*3]==pe[p] and board[i*3+1]==pe[p] and board[i*3+2]==pe[p]:
            win = True
        if board[i]==pe[p] and board[3+i]==pe[p] and board[6+i]==pe[p]:
            win = True
    if board[0] == pe[p] and board[4] == pe[p] and board[8] == pe[p]:
        win = True
    if board[2] == pe[p] and board[4] == pe[p] and board[6] == pe[p]:
        win = True
    if win:
        print("Player "+ pe[p]+ " wins!")
        break
    if valid:
        p = not p




