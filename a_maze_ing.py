#!/usr/bin/env python3
"""
Main module
"""

from sys import argv
from parser import ConfigParser
from visualizer import Visualizer


def a_maze_ing(argv: list[str]):
    parser = ConfigParser()
    try:
        parser.parse("config_vis.txt")
    except Exception as e:
        print("Error: ", e)

    vis = Visualizer()
    vis.read(parser.output_file)
    vis.render()


if __name__ == "__main__":
    a_maze_ing(argv)
