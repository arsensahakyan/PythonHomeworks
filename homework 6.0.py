import string


# Narek
#1
def colorOfSquare(square):
    if (string.ascii_lowercase.index(square[0].lower()) + 1) % 2 == int(square[1]) % 2:
        return 'black'
    else:
        return 'white'


def check(sq1, sq2):
    return colorOfSquare(sq1) == colorOfSquare(sq2)

# 2
def ek_pos(chess_board):
    ek_pos = []
    for row in chess_board:
        if 'ek' in row:
            ek_pos.append(chess_board.index(row))
            ek_pos.append(row.index('q'))
            break
    return ek_pos


def queen_position(chess_board):
    queen_pos = []
    for row in chess_board:
        if 'q' in row:
            queen_pos.append(chess_board.index(row))
            queen_pos.append(row.index('q'))
            break
    return queen_pos


def horizontal(chessboard, queen_pos):
    for elem in chessboard[queen_pos[0]]:
        if str(elem) not in 'qrek':
            chessboard[queen_pos[0]][chessboard[queen_pos[0]].index(elem)] = 'x'
    return chessboard


def vertical(chessboard, queen_pos):
    vert = [elem[queen_pos[1]] for elem in chessboard]
    for elem in vert:
        if str(elem) not in 'qrek':
            vert[vert.index(elem)] = 'x'
    for i in range(8):
        chessboard[i][queen_pos[1]] = vert[i]

    return chessboard


def diagonally1(chessboard, queen_pos):
    diag = []
    ind = []
    if queen_pos[1] - queen_pos[0] < 0:
        diag = [chessboard[i][i - abs(queen_pos[1] - queen_pos[0])] for i in
                range(abs(queen_pos[1] - queen_pos[0]), 9 - abs(queen_pos[1] - queen_pos[0]))]
        ind = [[i, i - abs(queen_pos[1] - queen_pos[0])] for i in range(abs(queen_pos[1] - queen_pos[0]), 8)]
    elif queen_pos[1] - queen_pos[0] > 0:
        diag = [chessboard[i][i + abs(queen_pos[1] - queen_pos[0])] for i in
                range(0, 8 - (queen_pos[1] - queen_pos[0]))]
        ind = [[i, i + abs(queen_pos[1] - queen_pos[0])] for i in range(0, 8 - (queen_pos[1] - queen_pos[0]))]
    else:
        diag = [chessboard[i][i] for i in range(8)]
        ind = [[i, i] for i in range(8)]

    for elem in diag:
        if str(elem) not in 'qrek':
            diag[diag.index(elem)] = 'x'

    for pos in ind:
        chessboard[pos[0]][pos[1]] = diag[ind.index(pos)]

    return chessboard


def diagonally2(chessboard, queen_pos):
    diag = []
    ind = []
    if 0 < queen_pos[0] + queen_pos[1] < 8:
        diag = [chessboard[i][queen_pos[0] + queen_pos[1] - i] for i in range(queen_pos[0] + queen_pos[1], -1, -1)]
        ind = [[i, queen_pos[0] + queen_pos[1] - i] for i in range(queen_pos[0] + queen_pos[1], -1, -1)]
    elif queen_pos[0] + queen_pos[1] > 7:
        diag = [chessboard[i][queen_pos[0] + queen_pos[1] - i] for i in range(7, queen_pos[0] + queen_pos[1] - 8, -1)]
        ind = [[i, queen_pos[0] + queen_pos[1] - i] for i in range(7, queen_pos[0] + queen_pos[1] - 8, -1)]

    for elem in diag:
        if str(elem) not in 'qrek':
            diag[diag.index(elem)] = 'x'
    for pos in ind:
        chessboard[pos[0]][pos[1]] = diag[ind.index(pos)]

    return chessboard


def rook(chessboard):
    rook_pos = []
    for row in chessboard:
        for col in row:
            if col == 'r':
                rook_pos.append([chessboard.index(row), row.index(col)])
    for pos in rook_pos:
        print(f' -- {chessboard[pos[0]]} -- ')
        for i in chessboard[pos[0]]:
            if str(i) not in 'qrek':
                chessboard[pos[0]][chessboard[pos[0]].index(i)] = 'x'
        for i in chessboard:
            if str(i[pos[1]]) not in 'qrek':
                i[pos[1]] = 'x'
    return chessboard


def isMate(chessboard):
    # rook
    rook(chessboard)

    # queen position
    queen_pos = queen_position(chessboard)

    diagonally2(chessboard, queen_pos)
    horizontal(chessboard, queen_pos)
    vertical(chessboard, queen_pos)
    diagonally1(chessboard, queen_pos)
    print(queen_pos)

    return chessboard


chessboard = [
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 'r', 0, 0, 0, 0, 0],
    [0, 0, 0, 'q', 0, 0, 'ek', 0],
    ['r', 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0]
]

cb = isMate(chessboard)
for elem in cb:
    print(elem)


# Ruben
# 1
def possible_turns(cell):
    letnum = string.ascii_lowercase.index(cell[0].lower())
    return_vals = []
    retval = []
    for i in -2, 2, 1, -1:
        if abs(i) == 2:
            return_vals.append(f'{string.ascii_lowercase[letnum + i].upper()}{int(cell[1]) + 1}')
            return_vals.append(f'{string.ascii_lowercase[letnum + i].upper()}{int(cell[1]) - 1}')
        else:
            return_vals.append(f'{string.ascii_lowercase[letnum + i].upper()}{int(cell[1]) - 2}')
            return_vals.append(f'{string.ascii_lowercase[letnum + i].upper()}{int(cell[1]) + 2}')
    for elem in return_vals:
        if not 0 < int(elem[1:]) < 9 or not -1 < string.ascii_lowercase.index(elem[0].lower()) < 8:
            retval.append(elem)
    return list(set(return_vals).difference(set(retval)))

# 2
def queen_position(chess_board):
    queen_pos = []
    for row in chess_board:
        if 'Q' in row:
            queen_pos.append(chess_board.index(row))
            queen_pos.append(row.index('Q'))
            break
    return queen_pos

def horizontal(chessboard, queen_pos):
    indexes = [0, 0]
    if chessboard[queen_pos[0]].count(1) == 1:
        if chessboard[queen_pos[0]].index(1) < chessboard[queen_pos[0]].index('Q'):
            for i in range(8):
                if chessboard[queen_pos[0]][i] != 1 and chessboard[queen_pos[0]][i] != 'Q' and chessboard[queen_pos[0]].index(1)<i:
                    chessboard[queen_pos[0]][i] = 'x'
        else:
            for i in range(8):
                if chessboard[queen_pos[0]][i] != 1 and chessboard[queen_pos[0]][i] != 'Q' and chessboard[queen_pos[0]].index(1)>i:
                    chessboard[queen_pos[0]][i] = 'x'
    elif chessboard[queen_pos[0]].count(1) > 1:
        for i in range(8):
            if chessboard[queen_pos[0]][i] == 1 and i < chessboard[queen_pos[0]].index('Q'):
                indexes[0] = i
            elif chessboard[queen_pos[0]][i] == 1 and i > chessboard[queen_pos[0]].index('Q'):
                indexes[1] = i
                break
        for i in range(indexes[0] + 1, indexes[1], 1):
            if chessboard[queen_pos[0]][i] != 'Q':
                chessboard[queen_pos[0]][i] = 'x'
    else:
        for i in range(0, 8):
            if chessboard[queen_pos[0]][i] != 'Q':
                chessboard[queen_pos[0]][i] = 'x'


    return chessboard

def vertical(chessboard, queen_pos):
    vert = [elem[queen_pos[1]] for elem in chessboard]
    indexes = [0, 0]
    if vert.count(1) == 1:
        if vert.index(1) > vert.index('Q'):
            for i in range(vert.index(1),-1,-1):
                if vert[i] != 'Q':
                    vert[i] = 'x'
        else:
            for i in range(vert.index(1)+1, 8):
                if vert[i] != 'Q':
                    vert[i] = 'x'
    elif vert.count(1) > 1:
        for i in range(8):
            if vert[i] == 1 and i < vert.index('Q'):
                indexes[0] = i
            elif vert[i] == 1 and i > vert.index('Q'):
                indexes[1] = i
                break

        for i in range(indexes[0] + 1, indexes[1], 1):
            if vert[i] != 'Q':
                vert[queen_pos[0]][i] = 'x'
    else:
        for i in range(8):
            if vert[i] != 'Q':
                vert[i] = 'x'

    for i in range(8):
        chessboard[i][queen_pos[1]] = vert[i]

    return chessboard

def diagonally1(chessboard, queen_pos):
    diag = []
    ind = []
    if queen_pos[1] - queen_pos[0] < 0:
        diag = [chessboard[i][i - abs(queen_pos[1] - queen_pos[0])] for i in range(abs(queen_pos[1] - queen_pos[0]), 9 - abs(queen_pos[1] - queen_pos[0]))]
        ind = [[i, i - abs(queen_pos[1] - queen_pos[0])] for i in range(abs(queen_pos[1] - queen_pos[0]), 8)]
    elif queen_pos[1] - queen_pos[0] > 0:
        diag = [chessboard[i][i + abs(queen_pos[1] - queen_pos[0])] for i in range(0, 8 - (queen_pos[1] - queen_pos[0]))]
        ind = [[i, i + abs(queen_pos[1] - queen_pos[0])] for i in range(0, 8 - (queen_pos[1] - queen_pos[0]))]
    else:
        diag = [chessboard[i][i] for i in range(8)]
        ind = [[i, i] for i in range(8)]

    indexes = [0, 0]
    if diag.count(1) == 1:
        if diag.index(1) > diag.index('Q'):
            for i in range(diag.index(1),-1,-1):
                if diag[i] != 'Q':
                    diag[i] = 'x'
        else:
            for i in range(diag.index(1)+1, len(diag)):
                if diag[i] != 'Q':
                    diag[i] = 'x'
    elif diag.count(1) > 1:
        for i in range(8):
            if diag[i] == 1 and i < diag.index('Q'):
                indexes[0] = i
            elif diag[i] == 1 and i > diag.index('Q'):
                indexes[1] = i
                break

        for i in range(indexes[0] + 1, indexes[1], 1):
            if diag[i] != 'Q':
                diag[i] = 'x'
    else:
        for i in range(len(diag)):
            if diag[i] != 'Q':
                diag[i] = 'x'

    for pos in ind:
        chessboard[pos[0]][pos[1]] = diag[ind.index(pos)]

    return chessboard

def diagonally2(chessboard, queen_pos):
    diag = []
    ind = []
    if 0 < queen_pos[0] + queen_pos[1] < 8:
        diag = [chessboard[i][queen_pos[0] + queen_pos[1] - i] for i in range(queen_pos[0] + queen_pos[1], -1, -1)]
        ind = [[i, queen_pos[0] + queen_pos[1] - i] for i in range(queen_pos[0] + queen_pos[1], -1, -1)]
    elif queen_pos[0] + queen_pos[1] > 7:
        diag = [chessboard[i][queen_pos[0] + queen_pos[1] - i] for i in range(7, queen_pos[0] + queen_pos[1] - 8, -1)]
        ind = [[i, queen_pos[0] + queen_pos[1] - i] for i in range(7, queen_pos[0] + queen_pos[1] - 8, -1)]

    indexes = [0, 0]
    if diag.count(1) == 1:
        if diag.index(1) > diag.index('Q'):
            for i in range(diag.index(1), -1, -1):
                if diag[i] != 'Q':
                    diag[i] = 'x'
        else:
            for i in range(diag.index(1) + 1, len(diag)):
                if diag[i] != 'Q':
                    diag[i] = 'x'
    elif diag.count(1) > 1:
        for i in range(8):
            if diag[i] == 1 and i < diag.index('Q'):
                indexes[0] = i
            elif diag[i] == 1 and i > diag.index('Q'):
                indexes[1] = i
                break

        for i in range(indexes[0] + 1, indexes[1], 1):
            if diag[i] != 'Q':
                diag[i] = 'x'
    else:
        for i in range(len(diag)):
            if diag[i] != 'Q':
                diag[i] = 'x'

    for pos in ind:
        chessboard[pos[0]][pos[1]] = diag[ind.index(pos)]

    return chessboard

def add_queen_possible_steps(chessboard):
    queen_pos = queen_position(chessboard)

    # horizontal
    horizontal(chessboard, queen_pos)

    # vertical
    vertical(chessboard, queen_pos)

    # diagonally 1
    diagonally1(chessboard, queen_pos)

    # diagonally 2
    diagonally2(chessboard, queen_pos)

    return chessboard

chess_board = [
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 'Q', 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0]
]
