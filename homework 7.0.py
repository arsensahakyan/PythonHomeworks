from itertools import permutations
import random

# Ruben
# 1
def swap_list_elements(nums):
    return_list = ['empty' for i in range(len(nums))]
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            for j in range(0, len(return_list), 2):
                if return_list[j] == 'empty':
                    return_list[j] = nums[i]
                    break
        else:
            for j in range(1, len(return_list), 2):
                if return_list[j] == 'empty':
                    return_list[j] = nums[i]
                    break
    return return_list


nums = [1, 4, 6, 5, 7, 10]

# 2
def get_count_of_rectangles(dict_of_points):
    squads = list(permutations(dict_of_points.keys(), 4))
    return_squads = []
    for squad in squads:
        x = 0
        y = 1
        A = dict_of_points[squad[0]]
        B = dict_of_points[squad[1]]
        C = dict_of_points[squad[2]]
        D = dict_of_points[squad[3]]
        if A[x] == B[x] and B[y] == C[y] and C[x] == D[x] and A[y] == D[y]:
            return_squads.append(''.join(sorted(list(squad))))
    return set(return_squads)


dict_of_points = {'A': (0, 0), 'B': (0, 4), 'C': (2, 0), 'D': (2, 4), 'E': (0, -4), 'F': (2, -4)}
print(get_count_of_rectangles(dict_of_points))

# Narek
# 1
def sorting(nums_and_trees):
    nt = sorted(nums_and_trees)[nums_and_trees.count(-1):]
    for num in nums_and_trees:
        if num == -1:
            nt.insert(nums_and_trees.index(-1), -1)
            nums_and_trees[nums_and_trees.index(-1)] = 0
    return nt


print(sorting([2, -1, 1, 5, 4, -1, 3]))

# 2
board = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 'w', 0, 'f', 0, 0, 0, 0, 0],
    [0, 0, 0, 10, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 'w', 0, 'f', 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 10, 0, 0, 0, 0]
]


def get_pos(board):
    return_value = []
    for row in board:
        for col in row:
            if str(col).isdigit() and col > 0:
                return_value.append([board.index(row), row.index(col)])
    return len(return_value), return_value

def get_neighbors(pos, board):
    return_val = dict()
    for i in range(pos[0] - 1, pos[0] + 2):
        for j in range(pos[1]-1, pos[1]+2):
            if 0 <= i < len(board) and 0 <= j < len(board[0]) and [i, j] != pos:
                if board[i][j] not in return_val.keys():
                    return_val[board[i][j]] = [[i, j]]
                else:
                    return_val[board[i][j]].append([i, j])
    return return_val


def step(pos, board):
    neighbors = get_neighbors(pos, board)
    poses = get_pos(board)
    num = board[pos[0]][pos[1]]
    if poses[0] == 2:
        poses[1].remove(pos)
        enemy_pos = poses[1][0]
        if board[enemy_pos[0]][enemy_pos[1]] in neighbors.keys():
            enemy = neighbors[poses[1].remove(pos)[0]][0]
            if board[pos[0]][pos[1]] > board[enemy[0]][enemy[1]]:
                board[pos[0]][pos[1]] -= board[enemy[0]][enemy[1]]
                board[enemy[0]][enemy[1]] = 'd'
                return board
            elif board[pos[0]][pos[1]] < board[enemy[0]][enemy[1]]:
                board[enemy[0]][enemy[1]] -= board[pos[0]][pos[1]]
                board[pos[0]][pos[1]] = 'd'
                return board
            else:
                board[pos[0]][pos[1]] = 'd'
                board[enemy[0]][enemy[1]] = 'd'
                return board
    if len(neighbors.keys()) == 1:
        random_number = int(random.uniform(0, len(neighbors[0])))
        p = neighbors[0][random_number]
        if list(neighbors.keys())[0] == 0:
            board[pos[0]][pos[1]] = 0
            if num > 1:
                board[p[0]][p[1]] = num - 1
            else:
                board[p[0]][p[1]] = 'd'
        elif list(neighbors.keys())[0] == 'w':
            board[pos[0]][pos[1]] = 0
            board[p[0]][p[1]] = num + 1
        else:
            board[pos[0]][pos[1]] = 0
            board[p[0]][p[1]] = num + 0.5
    elif len(neighbors.keys()) > 1:
        if 'w' in neighbors.keys():
            if len(neighbors['w']) == 1:
                p = neighbors['w'][0]
                board[pos[0]][pos[1]] = 0
                board[p[0]][p[1]] = num + 1
                return board
            else:
                random_number = int(random.uniform(0, len(neighbors['w'])))
                p = neighbors['w'][random_number]
                board[pos[0]][pos[1]] = 0
                board[p[0]][p[1]] = num + 1
                return board
        elif 'f' in neighbors.keys():
            if len(neighbors['f']) == 1:
                p = neighbors['f'][0]
                board[pos[0]][pos[1]] = 0
                board[p[0]][p[1]] = num + 0.5
                return board
            else:
                random_number = int(random.uniform(0, len(neighbors['f'])))
                p = neighbors['f'][random_number]
                board[pos[0]][pos[1]] = 0
                board[p[0]][p[1]] = num + 0.5
                return board
        else:
            if len(neighbors[0]) == 1:
                p = neighbors[0][0]
                board[pos[0]][pos[1]] = 0
                if num > 1:
                    board[p[0]][p[1]] = num - 1
                else:
                    board[p[0]][p[1]] = 'd'
                return board
            else:
                random_number = int(random.uniform(0, len(neighbors[0])))
                p = neighbors[0][random_number]
                if num > 1:
                    board[p[0]][p[1]] = num - 1
                else:
                    board[p[0]][p[1]] = 'd'
                return board


def game(board):
    pos = get_pos(board)

    while pos[0] > 0:
        if pos[0] == 2:
            step(pos[1][0], board)
            step(pos[1][1], board)
        else:
            step(pos[1][0], board)
        pos = get_pos(board)

    return board


print(*game(board), sep='\n')
