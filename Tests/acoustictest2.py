import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
from scipy.signal import fftconvolve
import IPython
import pyroomacoustics as pra

corners = np.array([[0,0], [0,3], [5,3], [5, 1], [3,1], [3,0]]).T
# first we make a room in 2-D
# room = pra.Room.from_corners(corners)
# fig, ax = room.plot()
# ax.set_ylim([-1, 6])
# ax.set_xlim([-1, 4])

# we can use the same geometry and extrude for 3-D
room = pra.Room.from_corners(corners)
# room.extrude(2.)
fig, ax = room.plot()
ax.set_xlim([0, 5])
ax.set_ylim([0, 3])
# ax.set_zlim([0, 2])

# specify a signal source
fs, signal = wavfile.read("FCJF0_SA1.wav")

# set max_order to a low value for a quick (but less accurate) RIR
room = pra.Room.from_corners(corners, fs=fs, max_order=8, absorption=0.2)
# room.extrude(2.)

# add source and set the signal to WAV file content
# room.add_source([1., 1., 0.5], signal=signal)   # in 3-D
room.add_source([1., 1.], signal=signal)          # in 2-D

# add two-microphone array
# R = np.array([[3.5, 3.6], [2., 2.], [0.5,  0.5]])  # [[x], [y], [z]]
# R = pra.circular_2D_array(center=[1.,2., 0.], M = 6, phi0=0, radius=0.1)
R = pra.circular_2D_array(center=[2.,2.], M=6, phi0=0, radius=0.1)

room.add_microphone_array(pra.MicrophoneArray(R, room.fs))

# compute image sources
room.image_source_model(use_libroom=True)

# visualize 3D polyhedron room and image sources
fig, ax = room.plot(img_order=6)
fig.set_size_inches(16/2, 9/2)

room.plot_rir()
fig = plt.gcf()
fig.set_size_inches(10, 5)

# room.simulate()
# print(room.mic_array.signals.shape)
#
# # original signal
# print("Original WAV:")
# IPython.display.Audio(signal, rate=fs)

# print("Simulated propagation to first mic:")
# IPython.display.Audio(room.mic_array.signals[0,:], rate=fs)

room.plot()
# command to actually show the plots
plt.show()

