import numpy as np


class FIRFilter:
    def __init__(self,b):
        self.order = len(b)
        self.b = b
        self.register = np.zeros(len(b))

    def Tick(self, x):
        self.register = np.roll(self.register,1)
        self.register[0] = x

        y = 0
        for x_n, b_n in zip(self.register, self.b):
            y += x_n*b_n
        return(y)

    def Reset(self):
        for n in range(self.order):
            self.register[n] = 0
