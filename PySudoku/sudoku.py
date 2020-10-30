# Import Modules
import os, pygame, copy, time
from pygame.locals import *
from pygame.compat import geterror
import sudokuSolver

if not pygame.font:
    print("Warning, fonts disabled")
if not pygame.mixer:
    print("Warning, sound disabled")

main_dir = os.path.split(os.path.abspath(__file__))[0]
data_dir = os.path.join(main_dir, "data")

# Test Array
test_array = [[0, 0, 0, 5, 7, 0, 8, 0, 9],
              [9, 0, 0, 0, 0, 0, 0, 4, 3],
              [3, 0, 7, 0, 0, 9, 2, 5, 1],
              [2, 0, 0, 0, 5, 8, 0, 1, 6],
              [0, 0, 0, 0, 0, 0, 0, 0, 0],
              [6, 7, 0, 9, 3, 0, 0, 0, 4],
              [1, 3, 9, 6, 0, 0, 4, 0, 5],
              [7, 2, 0, 0, 0, 0, 0, 0, 8],
              [8, 0, 4, 0, 2, 1, 0, 0, 0]]

###############
# Interaction #
###############

# Returns 0-8 cell location from mouse cords
def get_cur_cell(cur_loc):
    x_pos = int(cur_loc[0]/60)
    y_pos = int(cur_loc[1]/60)
    return (y_pos,x_pos)

# Advances a cell up to 9
def advance_cell(cur_cell, board, locked):
    y = cur_cell[0]
    x = cur_cell[1]
    if cur_cell not in locked:
        if board[y][x] < 9: 
            board[y][x] = board[y][x] + 1
        else:
            board[y][x] = 0

# Subtracts a cell down to 0
def subtract_cell(cur_cell, board, locked):
    y = cur_cell[0]
    x = cur_cell[1]
    if cur_cell not in locked:
        if board[y][x] > 0: 
            board[y][x] = board[y][x] - 1
        else:
            board[y][x] = 9

# Create locked cells list
def locked_cells(board):
    locked = []
    for y in range(9):
        for x in range(9):
            if board[y][x] != 0:
                locked.append((y,x))
    return locked

# Set everything not locked to 0
def reset_puzzle(board, locked):
    for i in range(9):
        for j in range(9):
            if (i,j) not in locked:
                board[i][j] = 0

# Run Solver and return a true or false, but not a solved puzzle
def check_puzzle(board):
    for i in range(9):
        for j in range(9):
            num = board[i][j]
            c_board = copy.deepcopy(board)
            c_board[i][j] = 0
            if not sudokuSolver.is_safe(c_board, num, i, j):
                return False
            elif num == 0:
                return False
    return True

###################        
# Draw the Screen #
###################
# Draw The Menu
def draw_menu():
    # Create The Background
    screen = pygame.display.set_mode((539, 539))
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((250, 250, 250))

    # Draw Text
    if pygame.font:
        font = pygame.font.Font(None, 36)
        options = ["1:Easy", "2:Medium", "3:Hard", "4:Blank", "5:Solve", "6:Reset", "7:Check Puzzle"] 
        y = 10
        for option in options:
            text = font.render(option, 1, (10, 10, 10))
            background.blit(text, (10,y))
            y += 25
    
    # Display The Background
    screen.blit(background, (0, 0))
    pygame.display.flip()

def draw_victory(status):
    # Create The Background
    screen = pygame.display.set_mode((539, 539))
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((250, 250, 250))

    # Draw Text
    if pygame.font:
        font = pygame.font.Font(None, 36)
        y = 10
        if status == True:
            text = font.render("Victory", 1, (10, 10, 10))
            background.blit(text, (10,25))
        else:
            text = font.render("Defeat", 1, (10, 10, 10))
            background.blit(text, (10,25))
            
    
    # Display The Background
    screen.blit(background, (0, 0))
    pygame.display.flip()
    # Lazy way to get the text to breifly appear on screen
    time.sleep(2)

# Breifly show instructions
def draw_inst():
    # Create The Background
    screen = pygame.display.set_mode((539, 539))
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((250, 250, 250))

    # Draw Text
    if pygame.font:
        font = pygame.font.Font(None, 36)
        inst = ["L/R cycles through numbers", "Esc for Menu"] 
        y = 10
        for i in inst:
            text = font.render(i, 1, (10, 10, 10))
            background.blit(text, (10,y))
            y += 25
    
    # Display The Background
    screen.blit(background, (0, 0))
    pygame.display.flip()
    # Lazy way to get the text to breifly appear on screen
    time.sleep(2)

def draw_solve(status):
    # Create The Background
    screen = pygame.display.set_mode((539, 539))
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((250, 250, 250))

    # Draw Text
    if pygame.font:
        font = pygame.font.Font(None, 36)
        y = 10
        if status == True:
            text = font.render("Solved", 1, (10, 10, 10))
            background.blit(text, (10,25))
        else:
            text = font.render("Not solvable in current state", 1, (10, 10, 10))
            background.blit(text, (10,25))
    
    # Display The Background
    screen.blit(background, (0, 0))
    pygame.display.flip()
    # Lazy way to get the text to breifly appear on screen
    time.sleep(2)

# Print The board state
def draw_board(board, locked):
    # Create The Background
    screen = pygame.display.set_mode((539, 539))
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((250, 250, 250))

    # Draw the Lines
    ## Big Grid
    for i in range(3):
        loc = 180*i
        pygame.draw.line(background, (0,0,0,0), (loc,0), (loc,539), 3)    
        pygame.draw.line(background, (0,0,0,0), (0,loc), (539,loc), 3)

    # Small grid
    for i in range(9):
        loc = 60*i
        pygame.draw.line(background, (0,0,0,0), (loc,0), (loc,539), 1)
        pygame.draw.line(background, (0,0,0,0), (0,loc), (539,loc), 1)

    # Draw the numbers, red for locked numbers, nothing if 0, black for user input numbers
    if pygame.font:
        font = pygame.font.Font(None, 36)
        y = 20
        for i in range(9):
            x = 20
            for j in range(9):
                num = board[i][j]
                if (i,j) in locked:
                    cell = font.render(str(num), 1, (255, 0, 0))
                    background.blit(cell, (x,y) )
                elif board[i][j] == 0:
                    cell = font.render(" ", 1, (10, 10, 10))
                    background.blit(cell, (x,y) )
                else:
                    cell = font.render(str(num), 1, (10, 10, 10))
                    background.blit(cell, (x,y) )
                x += 60
            y += 60
    
    # Display The Background
    screen.blit(background, (0, 0))
    pygame.display.flip()

###############    
# Main Method #
###############
def main():
    # Initialize Everything
    pygame.init()
    pygame.display.set_caption("Sudoku")
    pygame.mouse.set_visible(1)
    board = test_array
    locked = locked_cells(test_array)
    solved = []

    # Main Loop
    going = 3
    while going != 0:
        
        if going == 3:
            draw_inst()
            going = 2

        elif going == 1:
            # Handle input events
            for event in pygame.event.get():
                if event.type == QUIT:
                    going = 0
                # Back to Puzzle
                elif event.type == KEYDOWN and event.key == K_ESCAPE:
                    going = 2
                # Easy
                elif event.type == KEYDOWN and event.key == K_1:
                    solved = sudokuSolver.make_new_grid()
                    board = sudokuSolver.easy_puzzle(copy.deepcopy(solved))
                    locked = locked_cells(board)
                    going = 2
                # Medium
                elif event.type == KEYDOWN and event.key == K_2:
                    solved = sudokuSolver.make_new_grid()
                    board = sudokuSolver.medium_puzzle(copy.deepcopy(solved))
                    locked = locked_cells(board)
                    going = 2
                # Hard
                elif event.type == KEYDOWN and event.key == K_3:
                    solved = sudokuSolver.make_new_grid()
                    board = sudokuSolver.hard_puzzle(copy.deepcopy(solved))
                    locked = locked_cells(board)
                    going = 2
                # Blank
                elif event.type == KEYDOWN and event.key == K_4:
                    board = sudokuSolver.blank_grid()
                    locked = []
                    going = 2
                # Solve
                elif event.type == KEYDOWN and event.key == K_5:
                    draw_solve(sudokuSolver.solve_puzzle(board))
                    going = 2
                # Reset
                elif event.type == KEYDOWN and event.key == K_6:
                    reset_puzzle(board, locked)
                    going = 2
                # Check
                elif event.type == KEYDOWN and event.key == K_7:
                    print(check_puzzle(board))
                    draw_victory(check_puzzle(board))
                    going = 2
            draw_menu()

        elif going == 2:
            # Handle Input Events
            for event in pygame.event.get():
                if event.type == QUIT:
                    going = 0
                # Menu
                elif event.type == KEYDOWN and event.key == K_ESCAPE:
                    going = 1
                # Advance
                elif event.type == MOUSEBUTTONDOWN and event.button == 1:
                    cell = get_cur_cell(pygame.mouse.get_pos())
                    advance_cell(cell, board, locked)
                # Subtract
                elif event.type == MOUSEBUTTONDOWN and event.button == 3:
                    cell = get_cur_cell(pygame.mouse.get_pos())
                    subtract_cell(cell, board, locked)

            # Draw Everything
            draw_board(board, locked)

    pygame.quit()

if __name__ == "__main__":
    main()
