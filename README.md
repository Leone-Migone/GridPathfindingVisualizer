# Pathfinding Visualizer with Pygame

This is a simple pathfinding visualizer built using Python and Pygame. It demonstrates how **Breadth-First Search (BFS)** and **Depth-First Search (DFS)** algorithms explore a 2D grid to find a path between two user-defined points.

## Features

- Interactive 20×20 grid (each block is 30×30 pixels in 600x600 pixels window)
- Click to set **start** and **end** nodes (max 2 targets)
- Press `1` to visualize BFS
- Press `2` to visualize DFS
- Press any key after you have done a search to reset the grid
- Grid updates in real time showing:
  - **Red** squares as start/end targets
  - **Blue** squares as visited nodes
  - **Green** squares as part of the final path

## How to Run

1. Ensure you have Python 3 installed.
2. Install Pygame:

   ```bash
   pip install pygame

## Code Overview

### `Node` Class

Stores information about each cell in the grid:

- `rect`: The rectangle area of the node
- `visited`: If the node has been visited during search
- `weight`: Used for marking the path and potentially to implement weighted elements pathfinding
- `coordinates`: Position in grid
- `target`: Whether it's a start/end point
- `parent`: Used for backtracking the path

---

### Main Functions

- `main()`: Initializes pygame, handles the game loop and events.
- `gridlist()`: Creates the 2D list of nodes (grid).
- `clickedRect(pos)`: Adds clicked nodes to the target list.
- `draw()`: Draws the grid based on each node’s state.
- `BFS()` / `DFS()`: Runs Breadth-First Search or Depth-First Search.
- `trace_path(end_node)`: Traces the path from end to start using `.parent`.
- `resetGrid()`: Resets all nodes for a new search.
