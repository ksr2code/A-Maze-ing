"""
Maze generator using depth-first search algorithm.

Generates perfect mazes (no loops).
"""

from random import shuffle, seed


def dfs(maze) -> None:
    assert maze._entry is not None
    assert maze._height is not None
    assert maze._width is not None
    assert maze._grid is not None
    seed(maze._seed)
    stack: list[tuple[int, int]] = [maze._entry]
    visited: set[tuple[int, int]] = {maze._entry}
    neighbors = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    opposite_wall = [2, 3, 0, 1]
    dir = neighbors.copy()
    while stack:
        x, y = stack[-1]
        shuffle(dir)
        moved = False
        for dx, dy in dir:
            if 0 <= x + dx < maze._height and 0 <= y + dy < maze._width:
                if (x + dx, y + dy) not in visited:
                    stack.append((x + dx, y + dy))
                    visited.add((x + dx, y + dy))
                    i = neighbors.index((dx, dy))
                    maze._grid[x][y] &= ~(1 << i)
                    maze._grid[x + dx][y + dy] &= ~(1 << opposite_wall[i])
                    moved = True
                    break
        if not moved:
            stack.pop()
