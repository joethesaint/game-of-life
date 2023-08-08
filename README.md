# Conway's Game of Life Implementation in Python

Welcome to this repository containing an implementation of Conway's Game of Life in Python. This simple yet fascinating cellular automaton simulates the evolution of a grid of cells based on a set of rules. The game showcases emergent behavior as cells live, die, and reproduce over generations.

## Table of Contents

- [Introduction](#introduction)
- [Dependencies](#dependencies)
- [Installation](#installation)
- [Usage](#usage)
- [Example](#example)
- [Contributions](#contributions)
- [License](#license)

## Introduction

The provided code implements Conway's Game of Life, which is a cellular automaton devised by mathematician John Conway in 1970. The game consists of a grid of cells, each of which can be in one of two states: alive (1) or dead (0). The state of a cell evolves over generations according to the following rules:

1. Any live cell with fewer than two live neighbors dies (underpopulation).
2. Any live cell with two or three live neighbors lives on to the next generation.
3. Any live cell with more than three live neighbors dies (overpopulation).
4. Any dead cell with exactly three live neighbors becomes a live cell (reproduction).

These simple rules can lead to complex and captivating patterns.

## Dependencies

To run this implementation, you need:

- Python 3.x
- The `random` module (usually included in Python standard library)

## Installation

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/joethesaint/game-of-life-python.git
   cd game-of-life-python
   ```

2. Ensure you have Python 3.x installed. You can check by running:

   ```bash
   python3 --version
   ```

   If Python is not installed, you can download it from the official [Python website](https://www.python.org/downloads/).

## Usage

1. Navigate to the project directory containing the `game_of_life.py` file.

2. Open the `game_of_life.py` file in your preferred text editor or IDE.

3. Inside the file, you'll find a function `random_state(width, height)` which generates a random initial state for the game.

4. If you want to customize the grid size, modify the `width` and `height` parameters of the `random_state` function.

5. Run the `game_of_life.py` script using the following command:

   ```bash
   python3 game_of_life.py
   ```

6. The script will generate a random initial state and simulate the evolution of the grid based on the rules of Conway's Game of Life. Each generation will be printed to the console.

## Example

Here's a brief example of how to run the code:

```bash
git clone https://github.com/joethesaint/game-of-life-python.git
cd game-of-life-python
python3 game_of_life.py
```

You will see the grid evolve with each generation, displaying the changes in cell states over time.

## Contributions

Contributions to this repository are welcome! If you have any improvements or feature suggestions, feel free to fork this repository, make your changes, and submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Have fun exploring Conway's Game of Life and experimenting with different initial configurations! If you have any questions or run into issues, don't hesitate to ask for help.