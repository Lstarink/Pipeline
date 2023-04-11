import PDM
import CICFilter
import decimator
import movingFFT
import FIRFilter
import config

class PipelineMICTEST:
    def __init__(self):
        self.fft = movingFFT.MovingFFT(config.fft_order, config.fft_ts, config.fft_threshold, config.f_interest)
        self.FIR = FIRFilter.FIRFilter(config.FIRFilter_coefficients)

    def Tick(self, cic_out):
        fir = self.FIR.Tick(cic_out)
        return fir

