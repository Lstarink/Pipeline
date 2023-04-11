import numpy as np


class Goertzel:
    def __init__(self, N, fs, frequencies_of_interest, threshold):
        self.N = N
        self.fs = fs
        self.frequencies_of_interest = frequencies_of_interest
        self.threshold = threshold
        self.register = np.zeros([N])
        self.w0 = CalcW0(self)

    def Tick(self, x):
        self.register = np.roll(self.register,1)
        self.register[0] = x

        frequency_present = np.ones([len(self.frequencies_of_interest)], dtype=bool)
        for n, fn in enumerate(self.frequencies_of_interest):
            frequency_present[n] = Goertzel.CalcGoertzel(self, fn)

        return frequency_present

    def CalcGoertzel(self, fn):
        frequency_n_present = False

        return frequency_n_present

    def CalcW0(self):
        W0 = np.zeros([len(self.frequencies_of_interest)])
        frequency_bin = np.arange(self.N)
        list_of_possible_frequencies = np.linspace(0, 2*np.pi, self.N)
