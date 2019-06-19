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
fig, ax = room.plot()
ax.set_ylim([0, 10])
ax.set_xlim([0, 8])
ax.set_zlim([0, 5])
plt.show()

