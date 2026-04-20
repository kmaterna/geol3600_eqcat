import pandas as pd
import matplotlib.pyplot as plt

def lollipop_ts(earthquake):
	plt.plot(new_time, new_mag, marker = 'o')
	plt.xlabel("Date")
	plt.ylabel("Earthquake Magnitude")
	plt.grid(True)
 	plt.title("Earthquake Magnitude Time Series Plot")
	