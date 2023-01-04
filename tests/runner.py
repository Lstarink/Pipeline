import unittest

import test_pipeline
import test_CICFilter
import test_PDM
import test_movingFFT
import test_FIRFilter


def RunAllTests():
    verb = 2
    pipeline = unittest.TestLoader().loadTestsFromModule(test_pipeline)
    unittest.TextTestRunner(verbosity=verb).run(pipeline)

    CICFilter = unittest.TestLoader().loadTestsFromModule(test_CICFilter)
    unittest.TextTestRunner(verbosity=verb).run(CICFilter)

    pdm = unittest.TestLoader().loadTestsFromModule(test_PDM)
    unittest.TextTestRunner(verbosity=verb).run(pdm)

    fft = unittest.TestLoader().loadTestsFromModule(test_movingFFT)
    unittest.TextTestRunner(verbosity=verb).run(fft)

    fir = unittest.TestLoader().loadTestsFromModule(test_FIRFilter)
    unittest.TextTestRunner(verbosity=verb).run(fir)


if __name__ == "__main__":
    RunAllTests()