from abc import ABC, abstractmethod
import matplotlib.pyplot as plt


class Square(Rectangle):

    def __init__(self, side):
        super().__init__(side, side)