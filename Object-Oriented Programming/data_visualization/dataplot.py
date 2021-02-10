"""
I declare that the following source code was written solely by me. I understand that 
copying any source code, in whole or in part, constitutes cheating, and that I will 
receive a zero on this project if I am found in violation of this policy.
"""
__class__ = "CS 1410"
__project__ = "Project 6 - Data Visualization"
__author__ = "Ali Serdar Aydogdu"
__email__ = "lyonserdar@gmail.com"
__date__ = "2/9/2021"
__divider__ = "------------------------------------------------------------------------"

import glob
import matplotlib.pyplot as plt
import numpy as np


def analyze(fname):
    basename = fname[:-4]
    original = np.loadtxt(fname, dtype=np.int16)
    smoothed = np.zeros(original.size, dtype=np.int16)

    for i in range(original.size):
        weight = [1, 2, 3, 3, 3, 2, 1]
        weight_sum = sum(weight)
        if i < 4 or i > original.size - 4:
            smoothed[i] = original[i]
        else:
            smoothed[i] = np.dot(original[i - 3 : i + 4], weight) // weight_sum

    # Ploting
    _, axes = plt.subplots(nrows=2)
    xs = range(original.size)
    y_original = original
    y_smooth = smoothed
    axes[0].plot(xs, y_original)
    axes[0].set(title=fname, ylabel="original", xticks=[])
    axes[1].plot(xs, y_smooth)
    axes[1].set(ylabel="smoothed")
    plt.savefig(f"{basename}.pdf")

    pulse_positions = []
    i = 0
    rise = False
    while i < smoothed.size - 2:
        if smoothed[i] > smoothed[i + 1]:  # Check if not rising
            rise = False
        if not rise:  # If not previously rising
            if smoothed[i] < smoothed[i + 1] < smoothed[i + 2]:  # Check if rising
                if smoothed[i + 2] - smoothed[i] >= 100:  # Threshold (vt = 100)
                    rise = True
                    pulse_positions.append(i)
                    i += 2  # Go to next point
                    continue
        i += 1

    with open(f"{basename}.out", 'w+') as f:
        f.write(f"{fname}:\n")
        for index, position in enumerate(pulse_positions):
            area = 0
            point = position
            if index == len(pulse_positions) - 1:
                while point < original.size and point < position + 50:
                    area += original[point]
                    point += 1
            else:
                while point < position + 50 and point < pulse_positions[index + 1]:
                    area += original[point]
                    point += 1
            f.write(f"Pulse {index}: {position} ({area})\n")
        
            




def main():
    for fname in glob.glob("*.dat"):
        analyze(fname)


if __name__ == "__main__":
    print(__divider__)
    print(__project__)
    print(__divider__)
    main()
