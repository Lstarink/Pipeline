import numpy as np
import matplotlib.pyplot as plt

import config


class MovingFFT:
    def __init__(self, order, ts, treshold, f_interest):
        self.order = order
        self.ts = ts
        self.threshold = treshold
        self.plotting = False
        if type(f_interest)  == int:
            self.f_interest = [f_interest]
        else:
            self.f_interest = f_interest

        self.count = 0

        self.sampling_frequencies = np.fft.fftfreq(config.fft_order, self.ts)
        self.freq_index = MovingFFT.CalcFreqIndex(self)
        self.register = np.zeros(config.fft_order)
        self.fft_mag = np.zeros(config.fft_order)

    def CalcFreqIndex(self):
        freq_index = []
        for freq in self.f_interest:
            freq_index.append((np.abs(self.sampling_frequencies-freq)).argmin())
        return freq_index

    def Tick(self, x, plot = False):
        MovingFFT.Shift(self, x)
        MovingFFT.FFT(self)
        MovingFFT.Plot(self)
        return MovingFFT.Catch(self)


    def Shift(self, x):
        self.register = np.roll(self.register, 1)
        self.register[0] = x

    def FFT(self):
       fft = np.fft.fft(self.register)
       self.fft_mag = np.absolute(fft)

    def Plot(self):
        if self.plotting and self.count%20 == 0:
            plt.figure()
            plt.plot(self.sampling_frequencies, self.fft_mag)
            plt.show()

            plt.figure()
            plt.plot(np.arange(self.order)*self.ts, self.register)
            plt.show()
            self.plotting = input("keep plotting?")

            self.count = 0
        self.count += 1

    def Catch(self):
        freq_present = np.zeros(len(self.f_interest))
        for n, freq_index in enumerate(self.freq_index):
            if self.fft_mag[freq_index] > self.threshold:
                freq_present[n] = True
        return freq_present




if __name__ == "__main__":
    ts = 1/50
    fft = MovingFFT(100, ts, 10, 2)
    N = 1E3

    t = np.arange(0, N*ts, ts)
    f = 1*2*np.pi
    x = np.sin(f*t)


    for x_n in x:
        print(fft.Tick(x_n))
        plot = input("plot?")
        if plot:
            fft.Plot()

