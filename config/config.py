import scipy.io as sio
import numpy as np

fs = 4.8*1E6 #sampling frequency

#PDM
PDM_range = 1.5
#CIC_filter
cic_order = 16

#moving fft
fft_ts = cic_order/fs
fft_order = 512
fft_threshold = 75
f_interest = [35*1E3, 40*1E3, 30E3]

#FIRFilterCoefficients
file_location = '../firFilterCoeficients/newFilter.mat'
mat_contents = sio.loadmat(file_location)
coefficients_ = mat_contents["newFilter"]
FIRFilter_coefficients = np.array(coefficients_[0])

#FIRFilterCoefficients for IQ modulation
iq_file_location = '../firFilterCoeficients/LPF_coef_N200F5Wp200.mat'
iq_mat_contents = sio.loadmat(iq_file_location)
iq_coefficients_ = iq_mat_contents["LPF_coef_N200F5Wp200"]
IQ_FIRFilter_coefficients = np.array(coefficients_[0])

#Goertzel Filter
goertzel_threshold = 10
# fs = 4.8*1E6 #sampling frequency
#
# #PDM
# PDM_range = 1.5
# #CIC_filter
# cic_order = 8
#
# #moving fft
# fft_ts = cic_order/fs
# fft_order = 1000
# fft_threshold = 150
# f_interest = [35*1E3, 40*1E3, 30E3]
#
# #FIRFilterCoefficients
# mat_contents = sio.loadmat('LPF_coef_N200F6Wp50K.mat')
# coefficients_ = mat_contents["LPF_coef_N200F6Wp50K"]
# FIRFilter_coefficients = np.array(coefficients_[0])