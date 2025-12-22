"""
Parser for the maze
"""


from os import PathLike
from typing import Union


class ConfigParser:
    """
    Parser for the configuration file. The file must contain WIDTH, HEIGHT,
    ENTRY, EXIT, OUTPUT_FILE, PERFECT

    :param file: mandatory config.txt
    :type file: str
    :return: Returns a dictionary of either int or txt or of a Point class
    :rtype: dict[str, int | Point | str]
    """

    def __init__(self) -> None:
        self.width: None | int = None
        self.height: None | int = None
        self.entry: None | tuple[int, int] = None
        self.exit: None | tuple[int, int] = None
        self.output_file: Union[str, PathLike] = ""
        self.perfect: None | bool = None

    def parse(self, file):
        with open(file, "r") as fp:
            data = fp.read()
        for line in data.split("\n"):
            if line == "":
                continue
            key, val = line.split("=")
            if key == "WIDTH":
                self.width = int(val)
            if key == "HEIGHT":
                self.height = int(val)
            if key == "ENTRY":
                x, y = map(int, val.split(","))
                self.entry = (x, y)
            if key == "EXIT":
                x, y = map(int, val.split(","))
                self.exit = (x, y)
            if key == "OUTPUT_FILE":
                self.output_file = val
            if key == "PERFECT":
                self.perfect = True if val == "True" else False
