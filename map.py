import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def plot_map(long, lat, magnitude):
    plt.scatter(long, lat, size = magnitude)
    plt.xlabel("Longitude")
    plt.ylabel("Latitude")
    plt.title("Map of Longitude vs Latitude")
    plt.show()


 