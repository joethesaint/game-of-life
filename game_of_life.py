#!/usr/bin/python
import copy
import random
import time

def dead_state(width, height):
    return [[0 for _ in range(width)] for _ in range(height)] 

def random_state(width, height):
    state = dead_state(width, height)

    random_number = [[random.randint(0, 1) for _ in range(width)] for _ in range(height)]
    for i in range(height):
        for j in range(width):
            if random_number[i][j] >= 0.5:
                state[i][j] = 0
            else:
                state[i][j] = 1

    return state

def next_cell_value(cell_coords, state):
    # get the next value of a single cell in a state
    width = state_width(state)
    height = state_height(state)
    x = cell_coords[0]
    y = cell_coords[1]
    n_live_nebs = 0 # number of live neighbors

    # iterate around this cell's neighbors
    for x1 in range((x-1), (x+1)+1):
        # prevent going off the edge of the board
        if x1 < 0 or x1 >= width: continue

        for y1 in range((y-1), (y+1)+1):
            # prevent going off the edge of the board
            if y1 < 0 or y1 > height: continue
            # prevent counting the cell as a neighbor of itself!
            if x1 == x and y1 == y: continue

            if state[x1][y1] == 1: # LIVE
                n_live_nebs += 1

    if state[x][y] == 1: # LIVE
        if n_live_nebs <= 1:
            return 0 # DEAD
        elif n_live_nebs <= 3:
            return 1 # LIVE
        else:
            return 0 # DEAD
    else:
        if n_live_nebs == 3:
            return 1 # LIVE
        else:
            return 0 # DEAD

def state_width(state):
    # get the width of a state
    s_width = len(state)
    return s_width

def state_height(state): 
    # get the height of a state
    s_height = len(state[0])
    return s_height 


def render(board):
    for row in board:
        row_str = "|"
        for cell in row:
            if cell == 0:
                row_str += " "
            else:
                row_str += "#"
        row_str += "|"
        print(row_str)

def render(state):
    width = state_width(state)
    height = state_height(state)
    DEAD = 0
    LIVE = 1
    # displays a state by printing it to the terminal
    display_as = {
            DEAD: ' ',
            # This is "unicode" for a filled-in square. You can also just use a thick
            # "ASCII" character like a '$' or '#'.
            #LIVE: u"\u2588"
            LIVE: '$'
    }
    lines = []
    for y in range(0, height):
        line = ''
        for x in range(0, width):
            line += display_as[state[x][y]] * 2
        lines.append(line)
    print ("\n".join(line))

def next_board_state(board):
    height = len(board)
    width = len(board[0])
    new_state = dead_state(width, height) # Initialize a new state
    #new_state = [[0 for _ in range(width)] for _ in range(height)]

    for x in range(height):
        for y in range(width):
            current_cell_value = board[x][y]
            live_neighbors = count_live_neighbors(board, x, y)

            if current_cell_value == 1: # Live cell
                if live_neighbors < 2 or live_neighbors > 3:
                    new_state[x][y] = 0 # Dies due to underpopulation or overpopulation
                else:
                    new_state[x][y] = 1 # Stays alive
            else: # Dead cell
                if live_neighbors == 3:
                    new_state[x][y] = 1 # Becomes alive due to reproduction
        return new_state


def count_live_neighbors(board, x, y):
    live_neighbors = 0
    height = len(board)
    width = len(board[0])
    live_count = 0

    for i in range(-1, 2): # discover why it is this and what it reps **
        for j in range(-1, 2):
            if i == 0 and j == 0: # Skip the center cell itself
                continue
            new_x = x + i
            new_y = y + j
            if 0 <= new_x < height and 0 <= new_y < width:
                live_count += board[new_x][new_y]

    return live_count



def main():
    width = 20
    height = 4 

#    a_dead_state = dead_state(width, height)
#    print("Rendering a dead state:")
#    render(a_dead_state)

#    a_random_state = random_state(width, height)
#    print("\nRendering a random state:")
#    render(a_random_state)

    initial_state = random_state(width, height) # Initialize the initial state

    while True: # run the game forever
        render(initial_state) # print the current state
        new_state = next_board_state(initial_state) # Calculate the next
        time.sleep(1) # Optional: add a delay to control the speed of the animation
        initial_state = new_state # update the current state

def run_forever(init_state):
    next_state = init_state
    while True:
        render(next_state)
        next_state= next_board_state(next_state)
        time.sleep(1.03)

if __name__ == "__main__":
    #main()
    init_state = random_state(100, 50)
    #init_state = load_board_state('./toad.txt')
    run_forever(init_state)
            