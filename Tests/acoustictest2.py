import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
from scipy.signal import fftconvolve
import IPython
import pyroomacoustics as pra

corners = np.array([[0,0], [0,3], [5,3], [5, 1], [3,1], [3,0]]).T
# first we make a room in 2-D
room = pra.Room.from_corners(corners)
fig, ax = room.plot()
ax.set_ylim([-1, 6])
ax.set_xlim([-1, 4])

# we can use the same geometry and extrude for 3-D
room = pra.Room.from_corners(corners)
room.extrude(2.)
fig, ax = room.plot()
ax.set_xlim([0, 5])
ax.set_ylim([0, 3])
ax.set_zlim([0, 2])

# specify a signal source
fs, signal = wavfile.read("FCJF0_SA1.wav")

# add the source to our 3-D room
room = pra.Room.from_corners(corners, fs=fs)
room.extrude(2.)
room.add_source([1.,1.,0.], signal=signal)
fig, ax = room.plot()

ax.set_xlim([0, 5])
ax.set_ylim([0, 3])
ax.set_zlim([0, 2])

# command to actually show the plots
plt.show()