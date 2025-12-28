from random import seed, choice


def hak(maze) -> None:
    """
    Hunt-and-Kill maze generation algorithm using integer grid format.

    - Kill phase: random walk carving passages until stuck
    - Hunt phase: scan for an unvisited cell next to a visited one
    """

    assert maze._grid is not None
    assert maze._width is not None
    assert maze._height is not None
    assert maze._entry is not None

    seed(maze._seed)
    width = maze._width
    height = maze._height
    grid = maze._grid
    visited = set()
    DIRS = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    OPP = [2, 3, 0, 1]  # opposite wall index

    cx, cy = maze._entry
    visited.add((cx, cy))

    def kill(x, y):
        while True:
            neighbors = []

            for i, (dx, dy) in enumerate(DIRS):
                nx, ny = x + dx, y + dy
                if 0 <= nx < height and 0 <= ny < width:
                    if (nx, ny) not in visited:
                        neighbors.append((nx, ny, i))

            if not neighbors:
                return x, y

            nx, ny, i = choice(neighbors)

            grid[x][y] &= ~(1 << i)
            grid[nx][ny] &= ~(1 << OPP[i])

            visited.add((nx, ny))
            x, y = nx, ny

    def hunt():
        for x in range(height):
            for y in range(width):
                if (x, y) in visited:
                    continue

                candidates = []
                for i, (dx, dy) in enumerate(DIRS):
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < height and 0 <= ny < width:
                        if (nx, ny) in visited:
                            candidates.append((nx, ny, i))

                if candidates:
                    nx, ny, i = choice(candidates)

                    grid[x][y] &= ~(1 << i)
                    grid[nx][ny] &= ~(1 << OPP[i])

                    visited.add((x, y))
                    return x, y

        return None

    x, y = cx, cy
    while True:
        x, y = kill(x, y)
        found = hunt()
        if not found:
            break
        x, y = found
