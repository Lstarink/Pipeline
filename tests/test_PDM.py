import unittest
import PDM

class TestPDM(unittest.TestCase):
    def test_TickZero(self):
        pdm = PDM.PDM()
        self.assertEqual(pdm.Tick(0), -1)

    def test_Normalize(self):
        pdm = PDM.PDM(10)
        self.assertEqual(pdm.Normalize(8), .8)

    def test_Reset(self):
        pdm = PDM.PDM()
        pdm.Tick(0)
        self.assertNotEqual(0, pdm.error)
        pdm.Reset()
        self.assertEqual(0, 0)


if __name__ == '__main__':
    unittest.main()