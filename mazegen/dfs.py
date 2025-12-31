"""
Maze generator using depth-first search algorithm.

Generates perfect mazes (no loops).
"""

from random import shuffle, seed


def dfs(maze) -> None:
    assert maze.entry is not None
    assert maze.height is not None
    assert maze.width is not None
    assert maze.grid is not None

    # 42 pattern
    p42 = [
        [
            (
                1
                if (x - (maze.width // 2), y - (maze.height // 2))
                in [
                    (-3, -2),
                    (-1, -2),
                    (1, -2),
                    (2, -2),
                    (3, -2),
                    (-3, -1),
                    (-1, -1),
                    (3, -1),
                    (-3, 0),
                    (-2, 0),
                    (-1, 0),
                    (1, 0),
                    (2, 0),
                    (3, 0),
                    (-1, 1),
                    (1, 1),
                    (-1, 2),
                    (1, 2),
                    (2, 2),
                    (3, 2),
                ]
                else 0
            )
            for x in range(maze.width)
        ]
        for y in range(maze.height)
    ]

    seed(maze.seed)
    stack: list[tuple[int, int]] = [maze.entry]
    visited: set[tuple[int, int]] = {maze.entry}
    neighbors = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    opposite_wall = [2, 3, 0, 1]
    dir = neighbors.copy()
    while stack:
        x, y = stack[-1]
        shuffle(dir)
        moved = False
        for dx, dy in dir:
            if 0 <= x + dx < maze.height and 0 <= y + dy < maze.width:
                if p42[x + dx][y + dy]:
                    continue
                if (x + dx, y + dy) not in visited:
                    stack.append((x + dx, y + dy))
                    visited.add((x + dx, y + dy))
                    i = neighbors.index((dx, dy))
                    maze.grid[x][y] &= ~(1 << i)
                    maze.grid[x + dx][y + dy] &= ~(1 << opposite_wall[i])
                    moved = True
                    break
        if not moved:
            stack.pop()
