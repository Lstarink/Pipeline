import unittest
import matplotlib.pyplot as plt
import numpy as np
import config
import FIRFilter
import IQ as iq_filter


class TestIQ(unittest.TestCase):
    def test_Tick_zero_in_zero_out(self):
        iq = iq_filter.IQ(40E3, 6E5)
        in_phase, quadrature_phase = iq.Tick(0)

        self.assertEqual(in_phase, 0)
        self.assertEqual(quadrature_phase, 0)

    def test_Tick_mini_sim(self):
        signal_frequency = 40E3
        sampling_frequency = 6E6
        nr_of_periods_to_simulate = 16
        simulation_time = nr_of_periods_to_simulate/signal_frequency

        time_vector = np.arange(0, simulation_time, 1/sampling_frequency)
        theta = np.pi/3
        signal = np.sin(2*np.pi*signal_frequency*time_vector + theta)

        iq = iq_filter.IQ(signal_frequency, sampling_frequency)

        n = len(signal)
        in_phase_output = np.zeros(n)
        quadrature_phase_output = np.zeros(n)

        for n, x_n in enumerate(signal):
            in_phase_output[n], quadrature_phase_output[n] = iq.Tick(x_n)

        threshold = 1E-2
        self.assertLess(abs(np.mean(in_phase_output)-np.cos(theta)/2), threshold)
        print("in phase error: " + str(abs(np.mean(in_phase_output)-np.cos(theta)/2)))
        self.assertLess(abs(np.mean(quadrature_phase_output)-np.sin(theta)/2), threshold)
        print("quadrature phase error: " + str(abs(np.mean(quadrature_phase_output)-np.sin(theta)/2)))

        # plt.figure()
        # plt.plot(time_vector, signal)
        # plt.plot(time_vector, in_phase_output)
        # plt.plot(time_vector, quadrature_phase_output)
        # plt.show()

    def test_Tick_pulse_detection(self):
        signal_frequency = 40E3
        iq_frequency = 30E3
        sampling_frequency = 6E5
        nr_of_periods_to_simulate = 15
        simulation_time = nr_of_periods_to_simulate / signal_frequency

        FIR1 = FIRFilter.FIRFilter(config.IQ_FIRFilter_coefficients)
        FIR2 = FIRFilter.FIRFilter(config.IQ_FIRFilter_coefficients)

        time_vector = np.arange(0, simulation_time, 1 / sampling_frequency)
        theta = np.pi / 3
        signal = np.sin(2 * np.pi * signal_frequency * time_vector + theta)
        #2 * np.pi * signal_frequency * n/fs = 2pi - theta
        iq = iq_filter.IQ(iq_frequency, sampling_frequency)

        n = len(signal)
        in_phase_output = np.zeros(n)
        quadrature_phase_output = np.zeros(n)

        dc_in_phase = np.zeros(n)
        dc_quadrature_phase = np.zeros(n)

        for n, x_n in enumerate(signal):
            if 2*np.pi - theta > 2 * np.pi * signal_frequency * n/sampling_frequency:
                signal[n] = 0
                x_n = 0
            in_phase_output[n], quadrature_phase_output[n] = iq.Tick(x_n)
            dc_in_phase[n] = FIR1.Tick(in_phase_output[n])
            dc_quadrature_phase[n] = FIR2.Tick(quadrature_phase_output[n])

        # threshold = 1E-2
        # self.assertLess(abs(np.mean(in_phase_output) - np.cos(theta) / 2), threshold)
        # print("in phase error: " + str(abs(np.mean(in_phase_output) - np.cos(theta) / 2)))
        # self.assertLess(abs(np.mean(quadrature_phase_output) - np.sin(theta) / 2), threshold)
        # print("quadrature phase error: " + str(abs(np.mean(quadrature_phase_output) - np.sin(theta) / 2)))

        plt.figure()
        plt.plot(time_vector, signal)
        plt.plot(time_vector, in_phase_output)
        plt.plot(time_vector, quadrature_phase_output)
        plt.plot(time_vector, dc_in_phase)
        plt.plot(time_vector, dc_quadrature_phase)
        plt.show()


if __name__ == '__main__':
    unittest.main()