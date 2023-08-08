#!/usr/bin/python

from game_of_life import next_board_state
from game_of_life import dead_state

width = 3
height = 3

def test_dead_state():
    dead_state_result = dead_state(width, height)
    print(f"# TESTING DEAD STATE OF WIDTH:{width} AND HEIGHT:{height}")
    for row in dead_state_result:
        print(row)

def test_next_board_state():
    print("# TESTING THE NEXT BOARD STATE")
    initial_board = [
            [0, 1, 0],
            [0, 1, 0],
            [0, 1, 0]
    ]
    expected_next_state = [
            [0, 0, 0],
            [1, 1, 1],
            [0, 0, 0]
    ]

    actual_next_state = next_board_state(initial_board)

    print("Expected:")
    for row in expected_next_state:
        print(row)
    print("Actual:")
    for row in actual_next_state:
        print(row)

    assert actual_next_state == expected_next_state

    for x in range(len(initial_board)):
        for y in range(len(initial_board[0])):
            live_neighbors = count_live_neighbors(initial_board, x, y)
            print(f"At ({x}, {y}), live_neighbors: {live_neighbors}")

    print("All tests passed!")

def compare_states(expected, actual, test_number):
    if expected == actual:
        print(f"PASSED {test_number}")
    else:
        print(f"FAILED {test_number}")
        print("Expected:")
        print(expected)
        print("Actual:")
        print(actual)

    return test_number

def main():
    # TEST 1: dead cells with no live neighbors should stay dead.
    init_state1 = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
    ]
    expected_next_state1 = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
    ]
    print(f"# TEST 1: dead cells with no live neighbors should stay dead.")
    actual_next_state1 = next_board_state(init_state1)
    compare_states(expected_next_state1, actual_next_state1, 1)

    # TEST 2: dead cells with exactly 3 neighbors should come alive.
    init_state2 = [
            [0, 0, 1],
            [0, 1, 1],
            [0, 0, 0]
    ]
    expected_next_state2 = [
            [0, 1, 1],
            [0, 1, 1],
            [0, 0, 0]
    ]
    print(f"# TEST 2: dead cells with no live neighbors should stay dead.")
    actual_next_state2 = next_board_state(init_state2)
    compare_states(expected_next_state2, actual_next_state2, 2)

if __name__ == "__main__":
    main()
    test_dead_state()

