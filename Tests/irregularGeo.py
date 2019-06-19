# import the necessary libraries
import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
import pyroomacoustics as pra
import itertools as it
import ast

# we will try to replicate the ISPACE lab in pyroomacoustics
# this will test whether we can have objects in the room using the library
ispace_corners = np.array([[0,0],[1, 7.25], [8, 5.25], [7.75, 0]]).T
corners = np.array([[0,0], [0,3], [5,3], [5, 1], [3,1], [3,0]]).T


# first we make a room in 2-D
room = pra.Room.from_corners(ispace_corners)
room.extrude(3)
# fig, ax = room.plot()
# ax.set_ylim([0, 10])
# ax.set_xlim([0, 8])
# ax.set_zlim([0, 5])

# lets try to expand this to start simulating stuff in the I-space lab
# specify a signal source
fs, signal = wavfile.read("FCJF0_SA1.wav")

# set max_order to a low value for a quick (but less accurate) RIR
room = pra.Room.from_corners(ispace_corners, fs=fs, max_order=8, absorption=0.2)
room.extrude(3.)

# add source and set the signal to WAV file content
room.add_source([5., 5., 1.], signal=signal)  # in 3-D

# lets add a microphone array
R = np.array([[0.4, 0.4, 0.37, 0.43], [2.4, 2.4, 2.1, 2.7], [2.7, 2.4, 2.4, 2.4]])  # [[x], [y], [z]
room.add_microphone_array(pra.MicrophoneArray(R, room.fs))

# compute image sources
room.image_source_model(use_libroom=True)

# visualize 3D polyhedron room and image sources
fig, ax = room.plot(img_order=6)
fig.set_size_inches(16/2, 9/2)

ax.set_ylim([0, 10])
ax.set_xlim([0, 8])
ax.set_zlim([0, 5])
room.plot_rir()
fig = plt.gcf()
fig.set_size_inches(10, 5)

# lets try a new speaker position

# set max_order to a low value for a quick (but less accurate) RIR
room2 = pra.Room.from_corners(ispace_corners, fs=fs, max_order=8, absorption=0.2)
room2.extrude(3.)

# add source and set the signal to WAV file content
room2.add_source([0., 0., 1.], signal=signal)  # in 3-D

# lets add a microphone array
R = np.array([[0.4, 0.4, 0.37, 0.43], [2.4, 2.4, 2.1, 2.7], [2.7, 2.4, 2.4, 2.4]])  # [[x], [y], [z]
room2.add_microphone_array(pra.MicrophoneArray(R, room2.fs))

# compute image sources
room2.image_source_model(use_libroom=True)

# visualize 3D polyhedron room and image sources
fig, ax = room2.plot(img_order=6)
fig.set_size_inches(16/2, 9/2)

ax.set_ylim([0, 10])
ax.set_xlim([0, 8])
ax.set_zlim([0, 5])
room2.plot_rir()
fig = plt.gcf()
fig.set_size_inches(10, 5)

plt.show()

