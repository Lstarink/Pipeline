import unittest
import FIRFilter as fir
import numpy as np

class TestFIRFilter(unittest.TestCase):
    def test_Tick_FirstOrder(self):
        fir_filter = fir.FIRFilter([1])

        self.assertEqual(fir_filter.Tick(0), 0)
        self.assertEqual(fir_filter.Tick(1), 1)

    def test_Tick_SecondOrder(self):
        fir_filter = fir.FIRFilter([1,2])

        self.assertEqual(fir_filter.Tick(1), 1)
        self.assertEqual(fir_filter.Tick(1), 3)
        self.assertEqual(fir_filter.Tick(2), 4)
        self.assertEqual(fir_filter.Tick(2), 6)

    def test_Reset(self):
        fir_filter = fir.FIRFilter([1, 2])

        self.assertEqual(fir_filter.Tick(1), 1)
        self.assertEqual(fir_filter.Tick(1), 3)

        fir_filter.Reset()

        self.assertEqual(fir_filter.Tick(1), 1)
        self.assertEqual(fir_filter.Tick(1), 3)


if __name__ == '__main__':
    unittest.main()