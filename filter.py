import pandas as pd
def filter_bounds(eq,minlat,maxlat,minlong,maxlong):
	#Use a boolean index filtering line to transform the pd dataframe object into a filtered one within the bounds.
	#I thought I was going to have to do some crazy for loops to do this, but after some research apparently this is possible.
    bounded_eqs = eq[
    	(eq['latitude'] >= minlat) & 
        (eq['latitude'] <= maxlat) & 
        (eq['longitude'] >= minlon) & 
        (eq['longitude'] <= maxlon)]
    return bounded_eqs

def filter_time(eq,starttime,endtime)
	#Apply another boolean index filtering line. Hopefully my formatting is right for these.
	timed_eqs = eq[
        (eq['time'] >= start_time) & 
        (eq['time'] <= end_time)
    ]
    return timed_eqs

