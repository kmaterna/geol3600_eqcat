import pandas as pd
import matplotlib.pyplot as plt

def lollipop_ts(earthquakes):
	#extract time and magnitude from class
	new_time = [q.get_time() q in earthquakes]
	new_mag = [q.get_mag() for q in earthquakes]
	
	plt.plot(new_time, new_mag, marker = 'o')
	plt.xlabel("Date")
	plt.ylabel("Earthquake Magnitude")
	plt.grid(True)
 	plt.title("Earthquake Magnitude Time Series Plot")
	plt.show()
	