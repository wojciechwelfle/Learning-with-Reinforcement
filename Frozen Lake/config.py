# FILE TO CONFIG ENVIRONMENT

# Board
WIDTH = 10
HEIGHT = 10
DIRECTIONS = 4

# End states
END_STATE = [WIDTH - 1, HEIGHT - 1]
ACCEPTING_STATES = [[1, 1], [1, 3], [2, 3], [3, 0], [3, 3], [5, 5], [5, 6], [5, 7], [9, 8], [8, 8], [3, 6], [3, 7],
                    [2, 9], [3, 8], [8, 3], [7, 4], [5, 1], [6, 1]]
PENALTY = ACCEPTING_STATES
PENALTY_VALUE = -1

# Pixel Size
PIXEL_SIZE = 50
REFRESH_TIME = 75
