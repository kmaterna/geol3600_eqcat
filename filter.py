import pandas as pd

#I'm not sure how well the formatting matches up with how the read_cat function works,
#because that function returns individual arrays rather than a pd object, and a pd object is what my function requires.

def filter_bounds(eq,minlat,maxlat,minlong,maxlong):
	#Use a boolean index filtering line to transform the pd dataframe object into a filtered one within the bounds.
	#I thought I was going to have to do some crazy for loops to do this, but after some research apparently this is possible.
    bounded_eqs = eq[
    	(eq['lat'] >= minlat) & 
        (eq['lat'] <= maxlat) & 
        (eq['long'] >= minlon) & 
        (eq['long'] <= maxlon)]
    return bounded_eqs

def filter_time(eq,starttime,endtime)
	#Apply another boolean index filtering line.
	timed_eqs = eq[
        (eq['time'] >= start_time) & 
        (eq['time'] <= end_time)
    ]
    return timed_eqs

