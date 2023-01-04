import unittest
import CICFilter as cf
import numpy as np

class TestCICFilter(unittest.TestCase):
    def test_zero(self):
        filter = cf.CICFilter(1)
        self.assertEqual(filter.Tick(0), 0)

    def test_CALCOutput_FirstOrder_InputEqualsOutput(self):
        filter = cf.CICFilter(1)
        self.assertEqual(filter.Tick(5), 5)
        self.assertEqual(filter.Tick(-1), -1)

    def testCalcOutput_MovingAverage(self):
        filter = cf.CICFilter(4)
        input = range(1,10)
        output = np.array([1/4, 3/4, 6/4, 10/4, 14/4, 18/4, 22/4, 26/4, 30/4])

        for x, y in zip(input, output):
            y_ = filter.Tick(x)
            self.assertEqual(y_, y)



if __name__ == '__main__':
    unittest.main()