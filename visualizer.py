"""
Visualizer for the project

This will display the maze to stdout
"""

from enum import StrEnum
from sys import stdout


class WallGraphics(StrEnum):
    Hor = "─"
    Ver = "│"
    LTCor = "╭"
    LBCor = "╰"
    RTCor = "╮"
    RBCor = "╯"
    Cross = "┼"


class Color(StrEnum):
    Black = "30m"
    Red = "31m"
    Green = "32m"
    Yellow = "33m"
    Blue = "34m"
    Magenta = "35m"
    Cyan = "36m"
    White = "37m"
    Default = "39m"
    Reset = "0m"


class Cursor(StrEnum):
    Up = "1A"
    Down = "1B"
    Right = "1C"
    Left = "1D"
    Save = "7"
    Load = "8"


class Point:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y


class Cell(Point):
    def __init__(self, x, y, walls=0) -> None:
        super().__init__(x, y)
        self.walls = walls


class Maze:

    def __init__(self) -> None:
        self.maze: list[list[Cell]]
        self.start: Point
        self.end: Point
        self.path: list[str]

    def read(self, file: str) -> None:
        maze: list[list[Cell]] = []
        with open(file, "r") as fp:
            for y, line in enumerate(fp):
                if line == "\n":
                    break
                maze.append(
                    [
                        Cell(
                            x,
                            y,
                            int(c, 16),
                        )
                        for x, c in enumerate(line.strip())
                    ]
                )
            start = Point(*(int(x) for x in fp.readline().strip().split(",")))
            end = Point(*(int(x) for x in fp.readline().strip().split(",")))
            path = [c for c in fp.readline().strip()]
        self.maze = maze
        self.start = start
        self.end = end
        self.path = path


maze = Maze()
maze.read("output_maze.txt")
