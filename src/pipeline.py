import PDM
import CICFilter
import decimator
import movingFFT
import FIRFilter
import config

class Pipeline:
    def __init__(self):
        self.PDM = PDM.PDM(config.PDM_range)
        self.CIC = CICFilter.CICFilter(config.cic_order)
        self.dec = decimator.Decimator(config.cic_order)
        self.fft = movingFFT.MovingFFT(config.fft_order, config.fft_ts, config.fft_threshold, config.f_interest)
        self.FIR = FIRFilter.FIRFilter(config.FIRFilter_coefficients)

    def Tick(self, analog_in):
        pdm = self.PDM.Tick(analog_in)
        cic = self.CIC.Tick(pdm)

        if self.dec.UseSample():
            fir = self.FIR.Tick(cic)
            f_present = self.fft.Tick(fir)
            return f_present


