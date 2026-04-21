# Based on example earthquake catalogs from assignment. 
# I'm aware these maybe wouldn't work for every .csv or .catalog out there 

import pandas as pd

def read_cat(catalog):
    if catalog.endswith('.csv'):
        catalog_df = pd.read_csv(catalog)
        depth = catalog_df['depth']
        mag = catalog_df['mag']
        lat = catalog_df['latitude']
        long = catalog_df['longitude']
        time = catalog_df['time']
        return depth, mag, lat, long, time
    
    elif catalog.endswith('.catalog'):
        catalog_df = pd.read_csv(catalog, skiprows=9, sep='\s+')
        depth = catalog_df['DEPTH']
        mag = catalog_df['MAG']
        lat = catalog_df['LAT']
        long = catalog_df['LON']
        time = catalog_df['#YYY/MM/DD']
        return depth, mag, lat, long, time