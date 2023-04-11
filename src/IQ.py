import math as mt

class IQ:
    def __init__(self, frequency, sampling_frequency):
        self.frequency = frequency
        self.dt = 1/sampling_frequency
        self.time = 0

    def Tick(self, x_n):
        in_phase = mt.sin(2*mt.pi*self.frequency*self.time)*x_n
        quadrature_phase = mt.cos(2*mt.pi*self.frequency*self.time)*x_n
        self.time += self.dt
        return(in_phase, quadrature_phase)

    def Reset(self):
        self.time = 0