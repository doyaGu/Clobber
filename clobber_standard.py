def newBoard(n, p):
    board = []
    for y in range(p):
        row = []
        if y % 2 == 0:
            for x in range(n):
                row.append(x % 2 + 1)
            board.append(row)
        else:
            for x in range(n):
                row.append(((x % 2) ^ 1) + 1)
            board.append(row)
    return board


def display(board):
    def trans(num):
        if num == 0:
            return '.'
        else:
            return 'x' if num == 1 else 'o'
    for row in board:
        row_text = list(map(trans, row))
        print(' '.join(row_text))


def isInBoard(n, p, x, y):
    return 0 <= x < n and 0 <= y < p


def possiblePawn(board, n, p, player, i, j):
    return isInBoard(n, p, i, j) and board[j][i] == player


def getInput(string):
    try:
        num = int(input(string))
    except ValueError:
        print('Please enter a integer.')
        num = getInput(string)
    return num - 1


def selectPawn(board, n, p, player):
    print('Player {} : '.format(player))
    j = getInput('Select a pawn, row : ')
    i = getInput('Select a pawn, column : ')
    while not possiblePawn(board, n, p, player, i, j):
        j = getInput('Select a pawn, row : ')
        i = getInput('Select a pawn, column : ')
    return i, j


def possibleDestination(board, n, p, player, i, j, k, l):
    adversary = 2 if player == 1 else 1
    if isInBoard(n, p, k, l) and board[l][k] == adversary:
        return (i == k and abs(j - l) == 1) or (j == l and abs(i - k) == 1)
    return False


def selectDestination(board, n, p, player, i, j):
    l = getInput('Select a destination, row : ')
    k = getInput('Select a destination, column : ')
    while not possibleDestination(board, n, p, player, i, j, k, l):
        l = getInput('Select a destination, row : ')
        k = getInput('Select a destination, column : ')
    return k, l


def index(board, coordinate):
    return board[coordinate[1]][coordinate[0]]


def scope(coordinate):
    i, j = coordinate
    xs, ys = (i - 1, i + 1, i, i), (j, j, j - 1, j + 1)
    for i in range(4):
        yield xs[i], ys[i]


def getNeighbors(n, p, coordinate):
    neighbors = []
    for x, y in scope(coordinate):
            if isInBoard(n, p, x, y):
                neighbors.append((x, y))
    return neighbors


def again(board, n, p, player):
    continuance = False
    adversary = 2 if player == 1 else 1
    board_index = [(x, y) for x in range(n) for y in range(p)]
    for i in board_index:
        if index(board, i) == player:
            for neighbor in getNeighbors(n, p, i):
                if index(board, neighbor) == adversary:
                    continuance = True
    return continuance


def clobber(n, p):
    board = newBoard(n, p)
    player = 1
    while True:
        display(board)
        print('\n')
        i, j = selectPawn(board, n, p, player)
        k, l = selectDestination(board, n, p, player, i, j)
        board[j][i] = 0
        board[l][k] = player
        print('\n')
        if not again(board, n, p, player):
            break
        player = 2 if player == 1 else 1

    display(board)
    print('\n')
    if player == 2:
        print('Winner : 1')
    elif player == 1:
        print('Winner : 2')


if __name__ == '__main__':
    clobber(4, 3)
