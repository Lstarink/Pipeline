import unittest
import movingFFT
import numpy as np


class TestMovingFFT(unittest.TestCase):

    def test_TickZeros(self):
        order = 100
        ts = 1/10
        treshold = order/10
        f_interest = 5
        fft = movingFFT.MovingFFT(order, ts, treshold, f_interest)

        x = np.zeros(2*order)

        for x_n in x:
            frequency_present = fft.Tick(x_n)
            self.assertEqual(frequency_present, False)

    def test_TickSin(self):
        order = 100
        ts = 1 / 100
        treshold = 1
        f_interest = 5
        fft = movingFFT.MovingFFT(order, ts, treshold, f_interest)

        t = np.arange(2*order)*ts
        x = np.sin(2*f_interest*np.pi*t)

        for x_n, t_n in zip(x, t):
            frequency_present = fft.Tick(x_n)

            if t_n > 1/(f_interest):
                self.assertEqual(frequency_present, True)

    def test_TickNoise(self):
        order = 100
        ts = 1 / 100
        treshold = 1
        f_interest = 5
        fft = movingFFT.MovingFFT(order, ts, treshold, f_interest)

        x = np.random.randint(1, size=(order*2))

        for x_n in x:
            frequency_present = fft.Tick(x_n)
            self.assertEqual(frequency_present, False)



if __name__ == '__main__':
    unittest.main()
