# import the necessary libraries
import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
import pyroomacoustics as pra
import itertools as it
import ast

# lets take what we have learned in our tests to make an iterative approach for our acoustic simulation

# the idea, we consider a shoe box geometry by taking the maximum x, y, z coordinates and iterate through all xyz combo
# if the point is valid, then run the simulation for all microphones in the array.

# allow the user to add their own set of corners, max_order, absorption.
# eg: corners=[[0,0], [0,3], [5,3], [5, 1], [3,1], [3,0]], max_order=8, absorption=0.2
# user_corners = input("Input corners as an array of pairs [x,y] s.t. x and y form corner in your room:\n")

# allows us to convert string to list
# corners = ast.literal_eval(user_corners)

# user_max_order = int(input("Enter max order: "))
# user_absorption = float(input("Enter an absorption: "))

# or just do it manually for debugging
corners = [[0,0], [0,3], [5,3], [5, 1], [3,1], [3,0]]
user_max_order = 8
user_absorption = 0.67


# find the max of x and y coordinates
x_vals = [x for x,y in corners]
x_max = max(x_vals) + 1
y_vals = [y for x,y in corners]
y_max = max(y_vals) + 1

# use itertools to find all coordinates in the box
all_coords = list(it.product([i for i in range(x_max)], [j for j in range(y_max)]))

# set up pyroomacoustics variables
np_corners = np.array(corners).T
# specify a signal source
fs, signal = wavfile.read("FCJF0_SA1.wav")

results = []

for coord in all_coords:
    # set max_order to a low value for a quick (but less accurate) RIR
    room = pra.Room.from_corners(np_corners, fs=fs, max_order=user_max_order, absorption=user_absorption)

    # add source and set the signal to WAV file content
    room.add_source([1., 1.], signal=signal)  # in 2-D

    # add two-microphone array
    # R = np.array([[3.5, 3.6], [2., 2.]])  # [[x], [y], [z]]
    # or instead add circular microphone array
    R = pra.circular_2D_array(center=[2., 2.], M=6, phi0=0, radius=0.1)

    room.add_microphone_array(pra.MicrophoneArray(R, room.fs))


    # compute image sources
    room.image_source_model(use_libroom=True)

    fig, ax = room.plot(img_order=6)
    fig.set_size_inches(16 / 2, 9 / 2)

    room.plot_rir()
    fig = plt.gcf()
    # adjust the figure to show the plots in a viewable manner
    fig.set_size_inches(10, 5)
    plt.subplots_adjust(top=0.92, bottom=0.08, left=0.10, right=0.95, hspace=0.25,wspace=0.35)
    plt.suptitle(coord)
    ax = plt.gca()
    line = ax.lines[0]
#     results.append(line.get_xydata())
# print(results)
room.plot()
plt.show()









