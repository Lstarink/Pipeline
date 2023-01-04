import scipy.io as sio
import numpy as np

fs = 4.8*1E6 #sampling frequency

#PDM
PDM_range = 1.5
#CIC_filter
cic_order = 8

#moving fft
fft_ts = cic_order/fs
fft_order = 1000
fft_threshold = 150
f_interest = [35*1E3, 40*1E3, 30E3]

#FIRFilterCoefficients
mat_contents = sio.loadmat('LPF_coef_N200F6Wp50K.mat')
coefficients_ = mat_contents["LPF_coef_N200F6Wp50K"]
FIRFilter_coefficients = np.array(coefficients_[0])

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