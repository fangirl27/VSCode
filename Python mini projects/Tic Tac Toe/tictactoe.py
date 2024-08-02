print("Two player game for Tic Tac Toe. All inputs in the form a b only. ")
def Board():
    board = ['_' for j in range(9)]
        #self.current_winner = None
    final = [board[i*3:(i+1)*3] for i in range (3)]
    for row in  final:
        print('|' + '|'.join(row) + '|')
    return final

def player_input():
    p = input("Enter coordinates for playing: ")
    p = list(map(int, p.split()))
    while p[0] > 3 or p[1] > 3:
        print("Wrong input. Try again")
        p = input("Enter coordinates for playing: ")
        p = list(map(int, p.split()))
    return p

def check_winner(win, b):
    if b[0][0] == win and b[0][1] == win and b[0][2] == win:
        return 1
    elif b[1][0] == win and b[1][1] == win and b[1][2] == win:
        return 1
    elif b[2][0] == win and b[2][1] == win and b[2][2] == win:
        return 1
    elif b[0][0] == win and b[1][0] == win and b[2][0] == win:
        return 1
    elif b[0][1] == win and b[1][1] == win and b[2][1] == win:
        return 1
    elif b[0][2] == win and b[1][2] == win and b[2][2] == win:
        return 1
    elif b[0][0] == win and b[1][1] == win and b[2][2] == win:
        return 1
    elif b[0][2] == win and b[1][1] == win and b[2][0] == win:
        return 1
    else:
        return 0
    
def update_board(board, move, coords):
    row = coords[0]
    column = coords[1]
    while board[row][column] != '_':
        print("Wrong input.Try again")
        coords = player_input()
        row = coords[0]
        column = coords[1]
    board[row][column] = move
    return board

x = input("Player 1 choose symbol(x or o): ")
while x != 'x' and x != 'o':
    print("Wrong input")
    x = input("Player 1 choose symbol(x or o): ")
o = input("Player 2 choose symbol(x or o): ")
while o != 'x' and o != 'o':
    print("Wrong input")
    o = input("Player 2 choose symbol(x or o): ")
print("Game begins!")
print()

board = Board()
winner = 0

while winner == 0:
    counter = 0
    p1 = player_input()
    board = update_board(board, x, p1)
    for row in  board:
        print('|' + '|'.join(row) + '|')
    winner = check_winner(x, board)
    if winner == 1:
        print(f"Player 1({x}) wins")
        quit()
    for i in range(3):
        for j in range(3):
            if board[i][j] == '_':
                counter = counter + 1
    if counter == 0:
        print("Tie")
        quit()
    p2 = player_input()
    board = update_board(board, o, p2)
    for row in  board:
        print('|' + '|'.join(row) + '|')
    winner = check_winner(o, board)
    if winner == 1:
        print(f"Player 2({o}) wins")
        quit()
    for i in range(3):
        for j in range(3):
            if board[i][j] == '_':
                counter = counter + 1
    if counter == 0:
        print("Tie")
        quit()
            

