from abc import ABC
from abc import abstractmethod


class Step(ABC):
    def __init__(self):
        pass

    def process(self, data, inputs, utils, logger):
        pass


class StepException(Exception):
    pass
