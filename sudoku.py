import time
import random

grid = [[0 for x in range(9)] for y in range(9)]
game_type = ''

def solve(board):
    #find empty slot
    find = find_empty(board)
    #if no empty (0) slots, puzzle solved
    if not find:
        return True
    else:
        row, col = find
    #1-9 numbers
    for i in range(1,10):
        if valid(board, i, (row, col)):
            board[row][col] = i

            if solve(board):                
                return True
            board[row][col] = 0   
              
    return False
        
def valid(board, num, pos):
    # Check row
    for i in range(len(board[0])):
        if board[pos[0]][i] == num and pos[1] != i:
            return False

    # Check column
    for i in range(len(board)):
        if board[i][pos[1]] == num and pos[0] != i:
            return False

    # Check box
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x * 3, box_x*3 + 3):
            if board[i][j] == num and (i,j) != pos:
                return False

    return True


def generate_grid(q):
    count = 0
    start = time.time()
    print("Generating random puzzle....")
    while True:
        count += 1
        grid = [[0 for x in range(9)] for y in range(9)]
        rand_grid = [[0 for x in range(9)] for y in range(9)]   
        
        for i in range(q):
            row = random.randrange(9)
            col = random.randrange(9)
            num = random.randrange(1,10)
            while not valid(grid,num,(row,col)) or grid[row][col]!=0:
                row = random.randrange(9)
                col = random.randrange(9)
                num = random.randrange(1,10)
            grid[row][col]= num
            rand_grid[row][col]= num
        if solve(grid):
            end = time.time()
            print("Game Solved \n===================\n Random Grid\n===================")
            print_board(rand_grid)
            print("Solved Puzzle \n===================")
            print_board(grid)
            print(f"Puzzle generated in {end - start:0.4f} seconds")
            print(f"Attempts: {count}")
            return False


def print_board(board):
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")

        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")

def hello():

    print("Choose a level of Difficulty:")
    print("1. Beginner")
    print("2. Intermediate")
    print("3. Advanced")
    level = ""
    while not(level == 1 or level == 2 or level == 3):
        level = int(input())
    
    if level == 1:
        q = 30
    elif level == 2:
        q = 20
    else:
        q = 8
    
    print(q)
    return q
    

def find_empty(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i,j) #row, col
    return None 


print('''
Sudoku Game
==================
''') 
#choose to create a custom board or Random generated board
while not(game_type == "r" or game_type == "random" or game_type == "c" or game_type == "custom"):
    game_type = input("Custom board or Random board\n").lower()

if game_type == "r" or game_type == "random":
    print("Random Game Board:\n")
    q = hello()
    generate_grid(q)

elif game_type == "c" or game_type == "custom":
    print("Custom Game")
    grid = []
    while len(grid) < 9:

        row = list(input('Row: '))        
        #check input lenght is 9
        if len(row) != 9:
            print("row length must be equal to 9")
            continue        
        ints = []
        try:
            for i in row:            
                ints.append(int(i))
        except ValueError:
            print("Integers only.")
            continue
        grid.append(ints)
        print("Row " + str(len(grid)) + " complete")
    print_board(grid)
    print("Solving the board....")
    start = time.time()
    solve(grid)
    end = time.time()
    print("Solved Game\n==================")
    print_board(grid)
    print(f"Puzzle solved in {end - start:0.4f} seconds")
else:
    print("we done goofed")

#todo::
#gui