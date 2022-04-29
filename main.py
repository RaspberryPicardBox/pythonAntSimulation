"""
---An ant colony simulation written solely in Python---

Pixel "ants" will spread out from the colony home, trying to find food.
Ants will return home following pheromone paths when food has been found.

object types for now: air, ant, pheromone, food, colony

By Michael B
"""

import sys

# ---Constants---
WIDTH = 300
HEIGHT = 300
NUM_ANTS = 100


def help_func():
    print("""---An ant colony simulation written solely in Python---

    Pixel "ants" will spread out from the colony home, trying to find food.
    Ants will return home following pheromone paths when food has been found.
    
    Arguments:
    
    sizeX: int - size of window in x dimension
    sizeY: int - size of window in y dimension
    numAnts: int - number of ants
    """)


def main():
    global WIDTH
    global HEIGHT
    global NUM_ANTS

    # -- Handle arguments --
    args = sys.argv[1:]
    if "--help" in args or "--h" in args:
        help_func()
    else:
        try:
            for i in range(len(args)):
                if args[i] == "--sizeX":
                    WIDTH = args[i+1]
                elif args[i] == "--sizeY":
                    HEIGHT = args[i+1]
                elif args[i] == "--numAnts":
                    NUM_ANTS = args[i+1]
        except IndexError:
            sys.exit("Error in args, see --help")


if __name__ == '__main__':
    main()
