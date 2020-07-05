import random

def initialiseGrid():
    grid = [["O"] * 5] * 4  #4 rows by 5 columns grid for battleship
    for i in range(4):      #to avoid aliasing
        grid[i] = ["O"] * 5
    return grid

def displayGrid(grid):
    for row in grid:
        print("\t".join(row))
    print()

def validateRow(row):
    if not row.isdigit(): #presence and type check
        return False
    if int(row) < 0 or int(row) > 3: #range check
        return False
    return True

def validateCol(col):
    if not col.isdigit(): #presence and type check
        return False
    if int(col) < 0 or int(col) > 4: #range check
        return False
    return True

def checkResult(grid, row, col, ship_row, ship_col, won):
    if ship_row == row and ship_col == col: #player guessed correctly
        grid[row][col] = "S"
        won = True
    else:
        grid[row][col] = "X" #player guessed wrongly

    return won



