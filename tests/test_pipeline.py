import unittest

import config
import pipeline

class TestPipeline(unittest.TestCase):
    def test_zero(self):
        pl = pipeline.Pipeline()
        self.assertEqual(0,0 )


if __name__ == '__main__':
    unittest.main()
