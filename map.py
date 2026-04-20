import matplotlib.pyplot as plt

def plot_map(earthquakes):
    longitudes = []
    latitudes = []
    magnitudes = []

    # loop through each earthquake to get lat, long and magnitude
    for eq in earthquakes:
        longitudes.append(eq.longitude)
        latitudes.append(eq.latitude)
        magnitudes.append(eq.magnitude)

    # so points are visible on map
    sizes = []
    for mag in magnitudes:
        sizes.append(mag * 20)

    plt.scatter(longitudes, latitudes, s=sizes)
    plt.xlabel("Longitude")
    plt.ylabel("Latitude")
    plt.title("Earthquake Map")
    plt.show()