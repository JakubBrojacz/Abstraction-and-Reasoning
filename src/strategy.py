from enum import Enum

class ProcessingStrategy(Enum):
    # returns paths for the first input output only
    FIRST_ONLY = 1
    # generate one path, check for all input outputs, repeat for the next path
    ONE_BY_ONE = 2
