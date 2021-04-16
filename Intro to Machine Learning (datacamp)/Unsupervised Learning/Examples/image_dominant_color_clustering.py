#!/usr/bin/env python
# -*- coding: utf-8 -*-

# * Dominant colors in images

# Import libraries
import pandas as pd
from matplotlib import image as mpimg
from matplotlib import pyplot as plt
import seaborn as sns
import random

# Import models
from scipy.cluster.vq import kmeans
from scipy.cluster.vq import vq
from scipy.cluster.vq import whiten


image = mpimg.imread("batman.jpg")
print(image.shape)

r = []
g = []
b = []

for row in image:
    for pixel in row:
        temp_r, temp_g, temp_b = pixel
        r.append(temp_r)
        g.append(temp_g)
        b.append(temp_b)

pixels = pd.DataFrame({"red": r, "blue": b, "green": g})
print(pixels.head())

pixels["scaled_red"] = whiten(pixels["red"])
pixels["scaled_blue"] = whiten(pixels["blue"])
pixels["scaled_green"] = whiten(pixels["green"])


distortions = []
num_clusters = range(1, 11)

for i in num_clusters:
    cluster_centers, distortion = kmeans(
        pixels[["scaled_red", "scaled_blue", "scaled_green"]], i
    )
    distortions.append(distortion)

elbow_plot = pd.DataFrame({"num_clusters": num_clusters, "distortions": distortions})

sns.lineplot(x="num_clusters", y="distortions", data=elbow_plot)
plt.xticks(num_clusters)
plt.show()

cluster_centers, distortion = kmeans(
    pixels[["scaled_red", "scaled_blue", "scaled_green"]], 3
)

colors = []
r_std, b_std, g_std = pixels[["red", "blue", "green"]].std()

# Scale actual RGB values in range of 0 - 1
for cluster_center in cluster_centers:
    scaled_r, scaled_g, scaled_b = cluster_center
    colors.append(
        (scaled_r * r_std / 255, scaled_g * g_std / 255, scaled_b * b_std / 255)
    )

print(colors)
plt.imshow([colors])
plt.show()