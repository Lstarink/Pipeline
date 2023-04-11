import unittest

import config
import goertzel

class TestGoertzel(unittest.TestCase):
    def test_Tick_zero_input(self):
        N = 10

        goertzel_filter = goertzel.Goertzel(N, config.fs, config.f_interest, config.goertzel_threshold)
        frequency_present = goertzel_filter.Tick(0)

        for frequency_n_present in frequency_present:
            self.assertEqual(frequency_n_present, False)


if __name__ == '__main__':
    unittest.main()