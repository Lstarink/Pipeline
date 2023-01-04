import numpy as np

class CICFilter:
    def __init__(self, order):
        self.order = order
        self.input_register = np.zeros(order)
        self.output_register = 0

    def Tick(self, x_n):
        x_n = x_n/self.order
        y_n = x_n - self.input_register[-1] + self.output_register

        self.output_register = y_n
        self.input_register = np.roll(self.input_register,1)
        self.input_register[0] = x_n
        return(y_n)