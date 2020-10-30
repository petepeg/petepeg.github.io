########################################
### Sudoku Solver using backtracking ###
### Peter Pegues                     ###
########################################

##################
### The Solver ###
##################

## Check Subgrid
def in_subgrid(grid, num, row, col):
    row = row - row % 3
    col = col - col % 3
    for i in range(3):
        for j in range(3):
            if grid[i+row][j+col] == num:
                return True
    return False

## Check if safe
def is_safe(grid, num, row, col):
    # rotate Columns to rows
    r_grid = list(zip(*grid[::-1]))
    # make the check for rows and cols
    if num in grid[row] or num in r_grid[col]:
        return False
    # make the check for subgrids
    if in_subgrid(grid, num, row, col):
        return False
    
    return True

def find_empty_cell(grid, loc):
    for row in range(9):
        for col in range(9):
            if(grid[row][col] == 0):
                loc[0] = row
                loc[1] = col
                return True
    return False

# Returns True if solved False if no solution found
def solve_puzzle(grid):
    # Active location
    # List is used here specifically to take advantage of mutable properties of lists in python and their leaky scope
    loc = [0,0]
    
    # Look for an empty cell and set loc
    if find_empty_cell(grid,loc) == False:
        # No empty Cells, were done
        return True
    
    # Set loc based on result of find_empty_cell
    row = loc[0]
    col = loc[1]
    
    # Try and find a safe number
    for num in range(1,10):
        if is_safe(grid, num, row, col) == True:
            # set grid at location to current guess
            grid[row][col] = num
            # Recursively step through the grid
            if solve_puzzle(grid):
                return True
            # bad guess reset to 0
            grid[row][col] = 0
    
    # Backtrack
    return False

# Helper for Cleaner Console Printing
def print_puzzle(grid):
    print()
    for row in grid:
        print(row)

########################
### Sudoku Generator ###
########################
import random

## Generate random cordinate 0-8
def random_loc():
    return random.randint(0,8)

## Generate random 1-9
def random_int():
    return random.randint(1,9)

## Generate shuffled list of 1-9
def random_list():
    r_list = [1,2,3,4,5,6,7,8,9]
    random.shuffle(r_list)
    return r_list

## Blank Grid
def blank_grid():
    new_grid = [[0 for x in range(9)]for y in range(9)]
    return new_grid

## Create a valid random grid
## 30 was the fastest number of filled cells to gen a valid puzzle
## But this was too slow
def rand_grid():
    new_grid = blank_grid()
    row = random_loc()
    col = random_loc()
    num = random_int()
    for i in range(30):
        while new_grid[row][col] != 0 or not is_safe(new_grid, num, row, col):
            row = random_loc()
            col = random_loc()
            num =  random_int()
        
        new_grid[row][col] = num
    return new_grid

## Create a Valid grid with diagonal squares filled in
## Diag square are independent, this creates a puzzle with a higher chance of success
def diag_rand_grid():
    new_grid = [[0 for x in range(9)]for y in range(9)]
    row = 0
    col = 0
    for s in range(3):
        r_list = random_list()
        for i in range(3):
            for j in range(3):
                sf = s*3
                new_grid[sf+i+row][sf+j+col] = r_list.pop()
    return new_grid

## Try and solve a random grid, output on success, otherwise make a new puzzle     
def make_new_grid():
        x = 0
        new_grid = diag_rand_grid()
        while not solve_puzzle(new_grid):
            new_grid = diag_rand_grid()
            print("No solution %i"%(x))
            x += 1

        print("Success!\n")
        return new_grid

## Puzzle Pruner
def prune_grid(grid, n):
    row = random_loc()
    col = random_loc()
    for i in range(n):
        while grid[row][col] == 0:
            row = random_loc()
            col = random_loc()
        grid[row][col] = 0

    return grid

## Easy Puzzle
def easy_puzzle(grid):
    easy = prune_grid(grid, 43)
    return easy

## Medium Puzzle
def medium_puzzle(grid):
    medium = prune_grid(grid, 51)
    return medium

## Hard Puzzle
def hard_puzzle(grid):
    hard = prune_grid(grid, 56)
    return hard

## Custom Puzzle
def custom_puzzle(grid, n):
    custom = prune_grid(grid, n)
    return custom

###################
### Main Method ###
###################
import time

if __name__ == "__main__":
    # Test Puzzles
    solvable = [[0, 0, 0, 5, 7, 0, 8, 0, 9],
                [9, 0, 0, 0, 0, 0, 0, 4, 3],
                [3, 0, 7, 0, 0, 9, 2, 5, 1],
                [2, 0, 0, 0, 5, 8, 0, 1, 6],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [6, 7, 0, 9, 3, 0, 0, 0, 4],
                [1, 3, 9, 6, 0, 0, 4, 0, 5],
                [7, 2, 0, 0, 0, 0, 0, 0, 8],
                [8, 0, 4, 0, 2, 1, 0, 0, 0]]
    
    no_solution = [[5, 1, 6, 8, 4, 9, 7, 3, 2],
                   [3, 0, 7, 6, 5, 0, 0, 0, 0],
                   [8, 0, 9, 7, 0, 0, 0, 6, 5],
                   [1, 3, 5, 0, 6, 0, 9, 0, 7],
                   [4, 7, 2, 5, 9, 1, 0, 0, 6],
                   [9, 6, 8, 3, 7, 0, 0, 5, 0],
                   [2, 5, 3, 1, 8, 6, 0, 7, 4],
                   [6, 8, 4, 2, 0, 7, 5, 0, 0],
                   [7, 9, 1, 0, 5, 0, 6, 0, 8]]

    user_input = 0
    while user_input != "q":
        print("___________________________________")
        print("|   Sudoku Generator and Solver   |")
        print("|_________________________________|\n")

        print("Select an Option\n\n1:Easy Puzzle\n2:Medium Puzzle\n3:Hard Puzzle\n4:Custom Difficulty\n5:Solve a Puzzle\nq:Quit")
        user_input = str(input())

        if user_input == "q":
            print("Good Bye")
            break

        elif user_input == "1":
            start_time = time.time()
            solved = make_new_grid()
            print_puzzle(solved)
            print_puzzle(easy_puzzle(solved))
        
        elif user_input == "2":
            start_time = time.time()
            solved = make_new_grid()
            print_puzzle(solved)
            print_puzzle(medium_puzzle(solved))
        
        elif user_input == "3":
            start_time = time.time()
            solved = make_new_grid()
            print_puzzle(solved)
            print_puzzle(hard_puzzle(solved))
        
        elif user_input == "4":
            print("Enter desired number of empty cells")
            diff = int(input())
            while diff < 0 or diff > 81:
                print("Number was out of range, please enter a number between 0 and 81")
                diff = int(input())
            start_time = time.time()
            solved = make_new_grid()
            print_puzzle(custom_puzzle(solved, diff))
        
        elif user_input == "5":
            start_time = time.time()
            print("ToDO")
        
        else:
            start_time = time.time()
            print("You are eaten by a Grue")
        
        print("\n--- %s seconds ---\n" %(start_time - time.time()))


