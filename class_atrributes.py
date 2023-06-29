import random

class tic():
    board = ['_' for _ in range(9)]
    x = 0
    def __init__(self, x):
        self.board2 = ['_' for _ in range(9)]
        self.x = x
    
    def print_board(self):
        print("\t\tPRINT BOARD:")
        for i in range(3):
            print(f'\t\t{self.board[i*3]} {self.board[i*3 + 1]} {self.board[i*3 + 2]}')
        print("\n\t\tPRINT BOARD2")
        for i in range(3):
            print(f'\t\t{self.board2[i*3]} {self.board2[i*3 + 1]} {self.board2[i*3 + 2]}')

    def change_board(self, tac):
        self.board[tac] = 'X'

    def change_board2(self, toe):
        self.board2[toe] = 'O'
    
tic_1 = tic(5)
print(f'tic_1.x: {tic_1.x}')
tic_2 = tic(10)
print(f'tic_1.x: {tic_1.x}')
print(f'tic_2.x: {tic_2.x}')

# Initial boards
print("INITIAL BOARDS:\n")
print(f'\ttic_1:')
tic_1.print_board()

print(f'\n\ttic_2:')
tic_2.print_board()

# Boards after tic_1 change_boards
print("\n\nBoards after calling tic_1.change_board(0):\n")
tic_1.change_board(0)

print(f'\ttic_1:')
tic_1.print_board()

print(f'\n\ttic_2:')
tic_2.print_board()

# Boards after tic_2 change_boards
print("\n\nBoards after calling tic_2.change_board(8):\n")
tic_2.change_board(8)

print(f'\ttic_1:\n')
tic_1.print_board()

print(f'\n\ttic_2:\n')
tic_2.print_board()

# Boards after tic_1 change_boards2
print("\n\nBoards aftertic_1.change_board2(1):\n")
tic_1.change_board2(1)

print(f'\ttic_1:')
tic_1.print_board()

print(f'\n\ttic_2:')
tic_2.print_board()

# Boards after tic_2 change_boards2
print("\n\nBoards after calling tic_2.change_board2(7):\n")
tic_2.change_board2(7)

print(f'\ttic_1:')
tic_1.print_board()

print(f'\n\ttic_2:')
tic_2.print_board()

# Boards after tic_2 change_boards
print("\n\nBoards after calling tic_2.board:\n")
tic_2.board[5] = 'X'

print(f'\ttic_1:')
tic_1.print_board()

print(f'\n\ttic_2:')
tic_2.print_board()

print("\n")

tic_2.x = 15
tic_1.x = 21
print(f'tic_1.x : {tic_1.x}')
print(f'tic_2.x : {tic_2.x}')
print(f'id(tic_1.x) = {id(tic_1.x)}')
print(f'id(tic_2.x) = {id(tic_2.x)}')
print(f'id(tic_1.board) = {id(tic_1.board)}')
print(f'id(tic_2.board) = {id(tic_2.board)}')
print(f'id(tic_1.board2) = {id(tic_1.board2)}')
print(f'id(tic_2.board2) = {id(tic_2.board2)}')
