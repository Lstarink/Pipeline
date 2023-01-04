import numpy as np
import matplotlib.pyplot as plt

import pipeline as pl
import config

pipeline = pl.Pipeline()
t = np.arange(0, .1, 1/config.fs)
t_pulse = np.arange(0, 0.001, 1/config.fs)
N = len(t)

f1 = config.f_interest[0]
f2 = config.f_interest[1]
f3 = config.f_interest[2]

signal = np.zeros(len(t))
pulse1 = np.sin(2*np.pi*f1*t_pulse)
pulse2 = np.sin(2*np.pi*f2*t_pulse)
pulse3 = np.sin(2*np.pi*f3*t_pulse)

real_pulse_time_stamps1 = []
real_pulse_time_stamps2 = []
real_pulse_time_stamps3 = []

# Create a signal
for n, t_n in enumerate(t):
    signal[n]+= np.random.normal(0, .1)
    if (n % 5E4 == 0) and t_n < 0.09 and t_n!=0:
        real_pulse_time_stamps1.append(t_n)
        real_pulse_time_stamps2.append(t_n + 10E3/config.fs)

        signal[n:n+len(t_pulse)] += pulse1
        signal[int(n+10E3):int(n+len(t_pulse)+10E3)] += pulse2
    if (n % 7E4 == 0) and t_n < 0.09 and t_n!=0:
        real_pulse_time_stamps3.append(t_n)
        signal[n:n+len(t_pulse)] += pulse3

# for n, t_n in enumerate(t):
#     signal[n]+= np.random.normal(0, .1)
#     if (n % 7E4 == 0) and t_n < 0.09 and t_n!=0:
#         real_pulse_time_stamps1.append(t_n)
#         real_pulse_time_stamps2.append(t_n + 50E3/config.fs)
#         real_pulse_time_stamps3.append(t_n + 25E3/config.fs)
#         signal[n:n+len(t_pulse)] += pulse1
#         signal[int(n+50E3):int(n+len(t_pulse)+50E3)] += pulse2
#         signal[int(n+25E3):int(n+len(t_pulse)+25E3)] += pulse3


# plt.figure()
# plt.plot(t, signal)
# plt.show()
pulse_detected_vector = np.zeros([3, len(t)])
pulse_time_stamps = []

print(real_pulse_time_stamps1)
print(real_pulse_time_stamps2)
print(real_pulse_time_stamps3)

plot = False
show_pulse1 = np.zeros(len(t))
show_pulse2 = np.zeros(len(t))
show_pulse3 = np.zeros(len(t))

# plt.figure()
# plt.plot(t[int(0.072916666666*config.fs):int(0.072916666666*config.fs+0.001*config.fs)], signal[int(0.072916666666*config.fs): int(0.072916666666*config.fs+0.001*config.fs)])
# plt.show()

for n, x in enumerate(signal):
    pulse_detected = pipeline.Tick(x)

    if t[n] in real_pulse_time_stamps1 and t[n] > 0.07:
        pipeline.fft.plotting = False

    if pulse_detected is not None:
        for k, pulse_at_freq_k in enumerate(pulse_detected):
            if pulse_at_freq_k:
                pulse_time_stamps.append(t[n]*pulse_detected)
                pulse_detected_vector[k][n] = 1

    if t[n] in real_pulse_time_stamps1:
        show_pulse1[n] = 1

    if t[n] in real_pulse_time_stamps2:
        show_pulse2[n] = 1

    if t[n] in real_pulse_time_stamps3:
        show_pulse3[n] = 1

pulse_detected_timestamp = [[],[],[]]


for k in range(3):
    for n in range(len(t)):
        if pulse_detected_vector[k][n] and (1 not in pulse_detected_vector[k][n-len(pulse1):n-1]):
            pulse_detected_timestamp[k].append(t[n])


# plt.figure()
# plt.plot(t, pulse_detected_vector[0])
# plt.plot(t, show_pulse1)
# plt.show()
#
# plt.figure()
# plt.plot(t, pulse_detected_vector[1])
# plt.plot(t, show_pulse2)
# plt.show()
#
# plt.figure()
# plt.plot(t, pulse_detected_vector[2])
# plt.plot(t, show_pulse3)
# plt.show()
#
# plt.figure()
# plt.plot(t, show_pulse1)
# plt.plot(t, show_pulse2)
# plt.plot(t, show_pulse3)
# plt.show()

print(pulse_detected_timestamp)
pulse_real_timestamp = [real_pulse_time_stamps1, real_pulse_time_stamps2, real_pulse_time_stamps3]
time_difference = []

for i in range(3):
    for j in range(6):
        time_difference.append(pulse_real_timestamp[i][j]-pulse_detected_timestamp[i][j])

plt.figure()
plt.hist(time_difference)
plt.show()

print(time_difference)
print(np.mean(time_difference))
print(np.var(time_difference))