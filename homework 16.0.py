# 1
class User:
    def __init__(self, name):
        self.name = name

    def send_message(self, user, message):
        return f'"{message}" sent to {user.name}'

    def post(self, message):
        return f'{message} \n ***posted'

    def info(self):
        return ""

    def describe(self):
        classs = type(self).__name__
        return self.name, self.info()
        # if isinstance(self, Person):
        #     return self.name, Person.info(self)
        # elif isinstance(self, Community):
        #     return self.name, Community.info(self)
        # return self.name


class Person(User):
    def __init__(self, name, birthday):
        super().__init__(name)
        self.birthday = birthday

    def info(self):
        return self.birthday

    def subscribe(self, user):
        return f'Subscribed to {user.name}'


class Community(User):
    def __init__(self, name, description):
        super().__init__(name)
        self.description = description

    def info(self):
        return self.description


a = Person('arsen', '11.11.2020')
print(a.describe())


# 2
class TicTacToe:
    def __init__(self):
        self.board = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]

    def new_game(self):
        self.board = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]

    def get_field(self):
        print(self.board)

    def check_field(self):
        x = 'x'
        o = 'o'
        for i in range(len(self.board)):
            j = 0
            while j < len(self.board[0]) and self.board[i][j] == x:
                j += 1
            if j == len(self.board[0]):
                return x
        for k in range(len(self.board)):
            j = 0
            while j < len(self.board) and self.board[j][k] == x:
                j += 1
            if j == len(self.board):
                return x
        k = 0
        j = 0
        while j < len(self.board) and self.board[k][j] == x:
            j, k = j + 1, k + 1
        if j == len(self.board):
            return x
        k = 0
        j = len(self.board) - 1
        while j >= 0 and self.board[k][j] == x:
            j, k = j - 1, k + 1
        if j == -1:
            return x

        for i in range(len(self.board)):
            j = 0
            while j < len(self.board[0]) and self.board[i][j] == o:
                j += 1
            if j == len(self.board[0]):
                return o
        for k in range(len(self.board)):
            j = 0
            while j < len(self.board) and self.board[j][k] == o:
                j += 1
            if j == len(self.board):
                return o
        k = 0
        j = 0
        while j < len(self.board) and self.board[k][j] == o:
            j, k = j + 1, k + 1
        if j == len(self.board):
            return o
        k = 0
        j = len(self.board) - 1
        while j >= 0 and self.board[k][j] == o:
            j, k = j - 1, k + 1
        if j == -1:
            return o

        for i in range(len(self.board)):
            if '-' in self.board[i]:
                return None
        return 'D'

    def make_move(self, row, col):
        if self.board[row - 1][col - 1] != '-':
            return f"Cell {row}, {col} is already filled"
        else:
            count = 0
            for el in self.board:
                count += el.count('x')
                count -= el.count('o')
            if count == 0:
                self.board[row - 1][col - 1] = 'x'
            else:
                self.board[row - 1][col - 1] = 'o'

        if self.check_field() is None:
            return "Continue playing"
        elif self.check_field() == 'x':
            return "X-player won!"
        elif self.check_field() == 'x':
            return "O-player won"
        else:
            print("Game Over")
            return "Draw"

# t = TicTacToe()
# print(t.new_game())
# print(t.make_move(2, 2))
# t.get_field()
# print(t.make_move(2, 3))
# t.get_field()
# print(t.make_move(1, 1))
# t.get_field()
# print(t.make_move(1, 3))
# t.get_field()
# print(t.make_move(3, 3))
# t.get_field()
