# define function
def minesweeper_surrounding_mines(mine_map, mine):
    """ function which takes in a minesweeper map (2D list) and the character representing a mine, and returns a map
    showing each space in the grid's proximity to other mines and the position of the mines """
    # import required copy modules
    from copy import deepcopy

    # create variables storing grid size, a copy of the grid and an empty output map
    rows = len(mine_map)
    cols = len(mine_map[0])
    map_copy = deepcopy(mine_map)
    output_map = [[None] * cols for _ in range(rows)]

    # convert mines to 1s and empty spaces to 0s
    for row in range(rows):
        for col in range(cols):
            if map_copy[row][col] == mine:
                map_copy[row][col] = 1
            else:
                map_copy[row][col] = 0

    # add boundary layer of 0s to the mine map
    for row in map_copy:
        row.insert(0, 0)
        row.append(0)
    new_line = [0] * (cols + 2)
    map_copy.insert(0, new_line)
    map_copy.insert(-1, new_line)

    # return an output map showing mine positions and proximity to other mines
    for row in range(rows):
        for col in range(cols):
            # create plus-one variables to account for boundary layer
            row_plus_1 = row + 1
            col_plus_1 = col + 1
            # if the current iteration position in the grid is a mine, return the position of the mine to the output map
            if mine_map[row][col] == mine:
                output_map[row][col] = mine
            # if the current iteration position in the grid is not a mine, return surrounding mine count (as a string)
            else:
                output_map[row][col] = str(
                    map_copy[row_plus_1 - 1][col_plus_1 - 1]
                    + map_copy[row_plus_1 - 1][col_plus_1]
                    + map_copy[row_plus_1 - 1][col_plus_1 + 1]
                    + map_copy[row_plus_1][col_plus_1 - 1]
                    + map_copy[row_plus_1][col_plus_1 + 1]
                    + map_copy[row_plus_1 + 1][col_plus_1 - 1]
                    + map_copy[row_plus_1 + 1][col_plus_1]
                    + map_copy[row_plus_1 + 1][col_plus_1 + 1]
                )
    return output_map


# run function with supplied input
mine_map_input = [["-", "-", "-", "#", "#"],
                  ["-", "#", "-", "-", "-"],
                  ["-", "-", "#", "-", "-"],
                  ["-", "#", "#", "-", "-"],
                  ["-", "-", "-", "-", "-"]]
print(minesweeper_surrounding_mines(mine_map_input, "#"))

# run with different grid combination with more pound signs in the last two columns to show the program works
mine_map_input2 = [["-", "-", "-", "#"],
                   ["-", "#", "#", "#"],
                   ["-", "-", "#", "#"]]
print(minesweeper_surrounding_mines(mine_map_input2, "#"))

# run with a different grid combination and different symbols to prove dynamic code (if mines are dollar signs)
mine_map_input3 = [["-", "-", "$", "-", "-"],
                   ["$", "-", "-", "-", "$"],
                   ["-", "$", "-", "$", "-"],
                   ["-", "-", "-", "-", "$"],
                   ["-", "-", "$", "-", "-"],
                   ["$", "$", "-", "-", "$"]]
print(minesweeper_surrounding_mines(mine_map_input3, "$"))
